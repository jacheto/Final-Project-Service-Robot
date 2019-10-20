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
from roboserv_description.msg import AppMsg
from geometry_msgs.msg import PoseStamped

def update_AppMsg(appmsg):
	global AppMsg
	AppMsg = appmsg

def envia_pos():
	global AppMsg
	global goal_pub

	x_abs_px = AppMsg.robot_pos_x
	x_abs_px = AppMsg.robot_pos_y
	
	if not isinstance(goal_x, int) or not isinstance(goal_y, int):
		return
	
	screen_w = 200
	screen_h = 200
	prop = 0.25

	x_robot_px = screen_h * (1 - prop) - y_abs_px
	y_robot_px = x_abs_px - screen_w / 2

	x_robot_m = x_robot_px * resolution
	y_robot_m = y_robot_px * resolution
	
	ps = PoseStamped()
	goal_ang = 0
	(rx, ry, rz, rw) = tf.transformations.quaternion_from_euler(0, 0, goal_ang) 
	
	ps.pose.position.x = x_robot_m
	ps.pose.position.y = y_robot_m
	ps.pose.orientation.x = rx
	ps.pose.orientation.y = ry
	ps.pose.orientation.z = rz
	ps.pose.orientation.w = rw

	goal_pub.publish(ps)
    
def start():
	global goal_pub
	global navi_vel
	rospy.init_node('tratamento_pontos')
	rospy.Subscriber('appMsgs', AppMsg, update_AppMsg)
	goal_pub = rospy.Publisher('/move_base_simple/goal', PoseStamped, queue_size=1)
	
	rate = rospy.Rate(10)
	
	while not rospy.is_shutdown():
		envia_pos()
		rate.sleep()

if __name__ == '__main__':
    try:
        start()
    except rospy.ROSInterruptException:
        pass
