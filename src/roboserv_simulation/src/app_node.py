#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Software License Agreement (BSD License)
#
# Copyright (c) 2008, Willow Garage, Inc.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without

import rospy
import tf
import math
import os
import shutil
import json
import time
import requests
import subprocess
import shlex
import sys
import signal
import psutil
import cv2
import base64
from time import sleep
from six.moves import urllib
from roboserv_description.msg import AppMsg

class Roscore(object):
    """
    roscore wrapped into a subprocess.
    Singleton implementation prevents from creating more than one instance.
    """
    __initialized = False
    def __init__(self):
        if Roscore.__initialized:
            raise Exception("You can't create more than 1 instance of Roscore.")
        Roscore.__initialized = True
        self.rodando = False
    
    def run(self, command_list):
        try:
            self.roscore_process = subprocess.Popen(command_list)
            self.roscore_pid = self.roscore_process.pid  # pid of the roscore process (which has child processes)
            self.rodando = True
        except OSError as e:
            sys.stderr.write('roscore could not be run')
            raise e

    def terminate(self):
        logmsg("try to kill child pids of roscore pid: " + str(self.roscore_pid))
        kill_child_processes(self.roscore_pid)
        self.roscore_process.terminate()
        self.roscore_process.wait()  # important to prevent from zombie process
        Roscore.__initialized = False
        self.rodando = False

def logmsg(msg):
    rospy.loginfo(msg)

def kill_child_processes(parent_pid, sig=signal.SIGTERM):
    try:
        parent = psutil.Process(parent_pid)
        logmsg(parent)
    except psutil.NoSuchProcess:
        logmsg("parent process not existing")
        return
    children = parent.children(recursive=True)
    logmsg(children)
    for process in children:
        logmsg("try to kill child: " + str(process))
        process.send_signal(sig)

def post(chave, valor):
    logmsg("post called at '" + chave + "'")
    address = rospy.get_param('~server_address')
    valor_json = json.dumps(valor)
    try:
        requests.post(url = address + "/post_data?chave=" + chave, data=valor_json)
    except:
        logmsg("Aguardando Server")

def get(chave, obter_tempo=False):
    logmsg("get called at '" + chave + "'")
    address = rospy.get_param('~server_address')
    valor_json = ""
    try:
        valor_json = urllib.request.urlopen(address + '/get_data?chave=' + chave).read()
    except:
        logmsg("Aguardando Server")
    if valor_json == "":
        return "" if not obter_tempo else {'valor':"", 'tempo':0}
    
    valor_dict = json.loads(valor_json)
    logmsg(valor_dict)
    valor = valor_dict['valor']
    if obter_tempo:
        return {'valor': valor, 'tempo': valor_dict['timestamp_get'] - valor_dict['timestamp_post']}
    else:
        return valor



def loop():

    rospy.init_node('app_node')
    appMsg_pub = rospy.Publisher('appMsgs', AppMsg, queue_size=1)
    
    rate = rospy.Rate(1)
    
    directory = rospy.get_param('~directory')
    ard_port = rospy.get_param('~ard_port')
    map_dir = ""
    roscore = Roscore()
    app_ligado = False
    escolheu_mapa = False
    maps_list = []
    navigation_mode = 0
    robo_funcionando = False
    resetar_robo = False
    
    while not rospy.is_shutdown():

        # Avisa o App que o PC está ligado
        post("pc_on", True)
        post('navigation_mode', navigation_mode)
        # navigation_mode = 0 -> Não escolheu modo ainda
        # navigation_mode = 1 -> Modo localizacao
        # navigation_mode = 2 -> Modo mapeamento
        

        # Verifica se o App está ligado
        app_dict = get('app_on', True)
        if type(app_dict) is dict:
            app_ligado = app_dict['valor']
        else:
            app_ligado = False
        
        if not app_ligado:
            resetar_robo = True
            logmsg("aguardando app")
        
        else:
                
            if not escolheu_mapa:

                if not os.path.isdir(directory):
                    os.mkdir(directory)

                maps_list = os.listdir(directory)

                post('maps_list', maps_list)

                map_name = get('map_name')
                if map_name == "" or map_name == 'Key not available!':
                    logmsg("aguardando mapa")
                
                else:
                    if map_name.endswith('_del'):
                        dir_del = directory + '/' + map_name.replace('_del', '')
                        if os.path.isdir(dir_del):
                            shutil.rmtree(dir_del)
                            post('apagou_mapa', True)
                    else:
                        escolheu_mapa = True
            
            else:

                if not robo_funcionando:

                    map_dir = directory + '/' + map_name
                    map_app_dir = map_dir + "/map_img.jpg"

                    if map_name == "default":
                        if os.path.isdir(map_dir):
                            shutil.rmtree(map_dir)

                    if map_name in maps_list and map_name != "default":
                        # Modo localização
                        mapping = "false"
                        navigation_mode = 1
                    else:
                        # Modo mapeamento
                        mapping = "true"
                        navigation_mode = 2
                    
                    if not os.path.isdir(map_dir):
                            os.mkdir(map_dir)
                    
                    logmsg("Iniciando robo")
                    command_list = ['roslaunch', 'roboserv_simulation', 'roboserv_real.launch', 'map_name:=' + map_name, 'mapping:=' + mapping, 'maps_dir:=' + directory, 'ard_port:=' + ard_port]
                    roscore.run(command_list)
                    time.sleep(5)

                    robo_funcionando = True
                    
                else:
                    
                    # Envia o mapa atual
                    if os.path.exists(map_app_dir):
                        with open(map_app_dir,'rb') as image_jpg:
                            image_b64 = base64.encodestring(image_jpg.read())
                        post("map_64", 'data:image/jpg;base64,' + image_b64)
                    
                    # Obtem os comandos do app
                    operation_mode = get("operation_mode")
                    # operation_mode = 1 -> Seguir ponto no mapa definido pelo app
                    # operation_mode = 2 -> Navegacao manual
                    # operation_mode = 3 -> Navegacao autonoma
                    # operation_mode = 4 -> Parar movimentação
                    
                    # obtem o local onde o robo deve ir
                    robot_pos = get("robot_goal")
                    
                    # obtem os comandos dependendo de onde o usuario clicar no app
                    robot_commands = get("robot_commands")

                    # obtem o status do botao de desligar robo (a logica esta assim para impedir que 
                    # qualquer valor além de True seja considerado verdadeiro no 'if resetar_robo')
                    resetar_robo = True if get("turn_robot_off") == True else False

                    appMsg = AppMsg()
                    appMsg.operation_mode = operation_mode
                    appMsg.navigation_mode = navigation_mode
                    appMsg.button_up = robot_commands['up']
                    appMsg.button_down = robot_commands['down']
                    appMsg.button_left = robot_commands['left']
                    appMsg.button_right = robot_commands['right']
                    appMsg.button_up_left = robot_commands['up_left']
                    appMsg.button_up_right = robot_commands['up_right']
                    appMsg.button_down_left = robot_commands['down_left']
                    appMsg.button_down_right = robot_commands['down_right']
                    appMsg.robot_pos_x = robot_pos['x']
                    appMsg.robot_pos_y = robot_pos['y']

                    appMsg_pub.publish(appMsg)


            
            # Verifica se o último sinal de 'app ligado' foi enviado a mais de 5 segundos
            if app_dict['tempo'] > 5:
                operation_mode = 4
            
        if resetar_robo:
            if roscore.rodando:
                roscore.terminate()
            
            escolheu_mapa = False
            robo_funcionando = False
            post('map_name', '')
            resetar_robo = False

        rate.sleep()



if __name__ == '__main__':
    try:
        loop()
    except rospy.ROSInterruptException:
        pass
