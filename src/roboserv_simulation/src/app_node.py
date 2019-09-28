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
import requests
from time import sleep
from six.moves import urllib
from geometry_msgs.msg import Twist

address = 'http://192.168.1.2:5010' #rospy.get_param('~server_address')

def post(route, data):    
    requests.post(url = address + '/' + route, data=json.dumps(data))
    print("post de '" + str(data) + "' em " + route)

def get(route):
    valor = json.loads(urllib.request.urlopen(address + '/' + route).read())
    print("get de '" + str(valor) + "' em " + route)
    return valor

def loop():
    
    # Avisa que o PC ligou
    post("post_PC_on", {"PC_on":True})

    # Verifica se o app foi aberto
    app_on = False
    while not app_on:
        app_on = get('get_App_on')
        print("aguardando app")
        sleep(0.1)

    # Inicia modo escolha de mapa
    navigation_mode = 0
    post("post_navigation_mode", {"navigation_mode":navigation_mode})

    # Escolha dos mapas
    valid_map = False
    while not valid_map:

        directory = '/media/felipe/DATA/ROS_maps/roboserv' #rospy.get_param('~directory')
        if not os.path.isdir(directory):
            os.mkdir(directory)
        
        maps_list = []
        for subdir, dirs, files in os.walk(directory):
            maps_list.append(dirs[0])
        
        post("post_maps_list", {"maps_list":maps_list})

        map_name = ""
        while map_name == "":
            map_name = get("get_map_name")
            print("aguardando mapa")
            sleep(0.1)

        if map_name.endswith('_del'):
            shutil.rmtree(directory + '/' + map_name.replace('_del', ''))
            apagou_mapa = True
            post("post_apagou_mapa", {"post_apagou_mapa":apagou_mapa})
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
    
    print("BOOM")

    
    if not os.path.isdir(map_directory):
            os.mkdir(map_directory)

    

    # inicia ROS com os parâmetros map_name e mapping

    # verificar se o ROS já está aberto e rodando

    post("post_navigation_mode", {"navigation_mode":navigation_mode})


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
