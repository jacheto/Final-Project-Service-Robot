#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Software License Agreement (BSD License)
#
# Copyright (c) 2008, Willow Garage, Inc.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without

import rospy
from sensor_msgs.msg import Range
from geometry_msgs.msg import Twist
from roboserv_description.msg import AppMsg
from math import exp

range_F = 999
range_L = 999
range_R = 999
range_T = 999
input_vel = Twist()
last_input_vel = Twist()
last_output_vel = Twist()

def update_F(rng):
	global range_F
	range_F = rng.range

def update_L(rng):
	global range_L
	range_L = rng.range

def update_R(rng):
	global range_R
	range_R = rng.range

def update_vel(vel):
	global navi_vel
	navi_vel = vel

def update_AppMsg(appmsg):
	global AppMsg
	AppMsg = appmsg

def vel_mux():
	global range_F
	global range_L
	global range_R
	global range_T
	global vel_pub
	global navi_vel
	global last_input_vel
	global last_output_vel
	global AppMsg

	input_vel = Twist()
	
	if AppMsg.operation_mode == 1:
		input_vel = navi_vel

	elif AppMsg.operation_mode == 2:
    
		lin_vel = 0.2
		ang_vel = 0.8
		lin_vel_girando = 0.2
		ang_vel_girando = 0.2

		if AppMsg.button_up:
			input_vel.linear.x = lin_vel
			input_vel.angular.z = 0
		elif AppMsg.button_down:
			input_vel.linear.x = -lin_vel
			input_vel.angular.z = 0
		elif AppMsg.button_right:
			input_vel.linear.x = 0
			input_vel.angular.z = -ang_vel
		elif AppMsg.button_left:
			input_vel.linear.x = 0
			input_vel.angular.z = ang_vel
		elif AppMsg.button_up_right:
			input_vel.linear.x = lin_vel_girando
			input_vel.angular.z = -ang_vel_girando
		elif AppMsg.button_up_left:
			input_vel.linear.x = lin_vel_girando
			input_vel.angular.z = ang_vel_girando
		elif AppMsg.button_down_right:
			input_vel.linear.x = -lin_vel_girando
			input_vel.angular.z = -ang_vel_girando
		elif AppMsg.button_down_left:
			input_vel.linear.x = -lin_vel_girando
			input_vel.angular.z = ang_vel_girando
		

		#if min(range_F, range_L, range_R) < 0.3 and input_vel.linear.x > 0:
		#	input_vel.linear.x = 0

	elif AppMsg.operation_mode == 3:
		pass

	elif AppMsg.operation_mode == 4:
		input_vel = Twist()
	
	gate_control(input_vel)


def gate_control(input_vel):
	global range_F
	global range_L
	global range_R
	global range_T
	global vel_pub
	global last_input_vel
	global last_output_vel
	global AppMsg
	output_vel = Twist()
	
	# Aplica a rampa de velocidade
	max_acel_linear = 0.8
	max_acel_angular = 1

	if min(range_F, range_L, range_R) < 0.2 and input_vel.linear.x > 0:
		input_vel.linear.x = 0
	
	# Rampa linear
	max_acel_linear_fp = max_acel_linear / 20.0
	diff_linear = input_vel.linear.x - last_output_vel.linear.x

	if diff_linear != 0:
		signal_linear = diff_linear / abs(diff_linear)
	else:
		signal_linear = 1

	if abs(input_vel.linear.x - last_output_vel.linear.x) > max_acel_linear_fp:
		output_vel.linear.x = last_output_vel.linear.x + signal_linear * max_acel_linear_fp
	else:
		output_vel.linear.x = input_vel.linear.x
	
	# Rampa angular
	max_acel_angular_fp = max_acel_angular / 20.0
	diff_angular =  input_vel.angular.z - last_output_vel.angular.z

	if diff_angular != 0:
		signal_angular = diff_angular / abs(diff_angular)
	else:
		signal_angular = 1
	
	if abs(input_vel.angular.z - last_output_vel.angular.z) > max_acel_angular_fp:
		output_vel.angular.z = last_output_vel.angular.z + signal_angular * max_acel_angular_fp
	else:
		output_vel.angular.z = input_vel.angular.z
	
	last_output_vel = output_vel
	last_input_vel = input_vel
	
	gate_vel = Twist()

	# Evita deixar um numero muito pequeno
	if abs(output_vel.linear.x) < 1e-4:
		gate_vel.linear.x = 0
	else:
		gate_vel.linear.x = output_vel.linear.x

	if abs(output_vel.angular.z) < 1e-4:
		gate_vel.angular.z = 0
	else:
		gate_vel.angular.z = output_vel.angular.z
	
	# Publica a velocidade
	vel_pub.publish(input_vel)
    
def start():
	global vel_pub
	global navi_vel
	navi_vel = Twist()
	rospy.init_node('gate_control')
	rospy.Subscriber('distSensor_F', Range, update_F)
	rospy.Subscriber('distSensor_L', Range, update_L)
	rospy.Subscriber('distSensor_R', Range, update_R)
	rospy.Subscriber('cmd_vel_navi', Twist, update_vel)
	rospy.Subscriber('appMsgs', AppMsg, update_AppMsg)
	
	vel_pub = rospy.Publisher('cmd_vel_gate', Twist, queue_size=1)
	
	rate = rospy.Rate(20)
	
	while not rospy.is_shutdown():
		vel_mux()
		rate.sleep()

if __name__ == '__main__':
    try:
        start()
    except rospy.ROSInterruptException:
        pass
