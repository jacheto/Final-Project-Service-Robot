#!/usr/bin/env python
# Software License Agreement (BSD License)
#
# Copyright (c) 2008, Willow Garage, Inc.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without

import rospy
import tf
import math
from six.moves import urllib
import json
from geometry_msgs.msg import Twist


def read_entries():
    global vel
    address = 'http://192.168.1.2:5010' #rospy.get_param('~server_address')
    
    # inputs
    ambient_get = 'getAmbient'
    screen_position_get = 'getScreenPosition'
    
    # outputs
    robot_position_post = 'postRobotPosition'
    robot_map_post = 'postRobotMap'
    
    ambient = json.loads(urllib.request.urlopen(address + '/' + ambient_get).read())
    screen_position = json.loads(urllib.request.urlopen(address + '/' + screen_position_get).read())
    
    freq = 5
    lin_acel = 0
    ang_acel = 0
    
    robot_lin_acel = 0.2
    robot_ang_acel = 2

    robot_lin_vel = 0.2
    robot_ang_vel = 1

    lin_stop_time = 2
    ang_stop_time = 1.5
    
    if ambient["ambient"] == 'cozinha':
        lin_acel = 1
    else:
        lin_acel = 0
    
    if ambient["ambient"] == 'sala':
        ang_acel = 1
    else:
        ang_acel = 0

    if ambient["ambient"] == 'quarto':
        ang_acel = -1
    else:
        ang_acel = 0
    
    
    if vel.linear.x >= robot_lin_vel:
        vel.linear.x = robot_lin_vel
    elif vel.linear.x <= -robot_lin_vel:
        vel.linear.x = -robot_lin_vel
    else:
        vel.linear.x += lin_acel * robot_lin_acel / freq
    
    if vel.angular.z >= robot_ang_vel:
        vel.angular.z = robot_ang_vel
    elif vel.angular.z <= -robot_ang_vel:
        vel.angular.z = -robot_ang_vel
    else:
        vel.angular.z += ang_acel * robot_ang_acel / freq
    print(vel.angular.z)
    print(vel.linear.x)
    print('---')
    
    if vel.linear.x > 0 and vel.angular.z > 0:
        vel_pub.publish(vel)
    
    vel.linear.x  -= 1 / (freq * lin_stop_time)
    vel.angular.z -= 1 / (freq * ang_stop_time)


def begin():
    global vel_pub
    global vel
    rospy.init_node('comunicacao_server')
    vel_pub = rospy.Publisher('cmd_vel_mux/input/teleop', Twist, queue_size=1)

    vel = Twist()
    rate = rospy.Rate(5)

    while not rospy.is_shutdown():
        read_entries()

        rate.sleep()
	
if __name__ == '__main__':
    try:
        begin()
    except rospy.ROSInterruptException:
        pass
