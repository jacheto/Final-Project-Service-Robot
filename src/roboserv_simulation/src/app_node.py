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
from geometry_msgs.msg import Twist

def kill_child_processes(parent_pid, sig=signal.SIGTERM):
    try:
        parent = psutil.Process(parent_pid)
        print(parent)
    except psutil.NoSuchProcess:
        print("parent process not existing")
        return
    children = parent.children(recursive=True)
    print(children)
    for process in children:
        print("try to kill child: " + str(process))
        process.send_signal(sig)

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
    def run(self, command_list):
        try:
            self.roscore_process = subprocess.Popen(command_list)
            self.roscore_pid = self.roscore_process.pid  # pid of the roscore process (which has child processes)
        except OSError as e:
            sys.stderr.write('roscore could not be run')
            raise e
    def terminate(self):
        print("try to kill child pids of roscore pid: " + str(self.roscore_pid))
        kill_child_processes(self.roscore_pid)
        self.roscore_process.terminate()
        self.roscore_process.wait()  # important to prevent from zombie process
        Roscore.__initialized = False



def post(chave, valor):
    address = "http://10.0.0.2:5010"
    valor_json = json.dumps({'valor': valor, 'timestamp':time.time()})
    requests.post(url = address + "/post_data?chave=" + chave, data=valor_json)

def get(chave, get_timestamp=False):
    address = "http://10.0.0.2:5010"
    valor_json = urllib.request.urlopen(address + '/get_data?chave=' + chave).read()
    if valor_json == "":
        return ""
    valor_dict = json.loads(valor_json)
    if get_timestamp:
        return valor_dict


def loop():
    
    # Avisa que o PC ligou
    post("pc_on", True)

    # Verifica se o app foi aberto
    app_on = False
    while not app_on:
        app_on = get('app_on')
        print("aguardando app")
        sleep(0.1)

    # Inicia modo escolha de mapa
    navigation_mode = 0
    post('navigation_mode', navigation_mode)

    # Escolha dos mapas
    valid_map = False
    while not valid_map:

        directory = '/media/felipe/DATA/ROS_maps/roboserv' #rospy.get_param('~directory')
        if not os.path.isdir(directory):
            os.mkdir(directory)
        
        maps_list = []
        for subdir, dirs, files in os.walk(directory):
            maps_list.append(dirs[0])
        
        post('maps_list', maps_list)

        map_name = ""
        while map_name == "":
            map_name = get('map_name')
            print("aguardando mapa")
            sleep(0.1)

        if map_name.endswith('_del'):
            shutil.rmtree(directory + '/' + map_name.replace('_del', ''))
            apagou_mapa = True
            post('apagou_mapa', True)
        else:
            valid_map = True
    

    map_directory = directory + '/' + map_name

    if map_name == "default":
        if os.path.isdir(map_directory):
            shutil.rmtree(map_directory)

    if maps_list.__contains__(map_name) and map_name != "default":
        mapping = "false"
        navigation_mode = 1
    else:
        mapping = "true"
        navigation_mode = 2
    
    if not os.path.isdir(map_directory):
            os.mkdir(map_directory)
    
    # inicia ROS com os parâmetros map_name e mapping

    roscore = Roscore()
    
    command_list = ['roslaunch', 'roboserv_simulation', 'roboserv_real.launch', 'map_name:="' + map_name + '"', 'mapping:="' + mapping + '"']
    roscore.run(command_list)
    time.sleep(5)

    post('navigation_mode',navigation_mode)

    if navigation_mode == 1:
        post('localization_status', 0)



    # envio do mapa

    filename_pgm = ""
    filename_jpg = ""
    image_pgm = cv2.imread(filename_pgm)
    cv2.imwrite(filename_jpg, image_pgm)
    image_jpg = open(filename_jpg, 'rb')
    image_b64 = base64.encodestring(image_jpg.read())
    post("map_64", image_b64)



    #roscore.terminate()

    # verificar se o ROS já está aberto e rodando



def begin():
    global vel_pub
    global vel
    rospy.init_node('app_node')
    vel_pub = rospy.Publisher('cmd_vel_mux/input/teleop', Twist, queue_size=1)

    vel = Twist()
    rate = rospy.Rate(20)

    while not rospy.is_shutdown():
        loop()

        rate.sleep()
	
if __name__ == '__main__':
    try:
        begin()
    except rospy.ROSInterruptException:
        pass
