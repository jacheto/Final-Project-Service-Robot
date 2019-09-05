#!/usr/bin/env python
# Software License Agreement (BSD License)
#
# Copyright (c) 2008, Willow Garage, Inc.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without

import rospy
from sensor_msgs.msg import Range
from geometry_msgs.msg import Twist

range_R = 999
range_FR = 999
range_F = 999
range_FL = 999
range_L = 999
input_vel = Twist()
last_input_vel = Twist()
last_output_vel = Twist()

def update_R(rng):
	global range_R
	range_R = rng.range

def update_FR(rng):
	global range_FR
	range_FR = rng.range

def update_F(rng):
	global range_F
	range_F = rng.range

def update_FL(rng):
	global range_FL
	range_FL = rng.range

def update_L(rng):
	global range_L
	range_L = rng.range
	
def update_vel(vel):
	global input_vel
	input_vel = vel;

def gate_control():
	global range_R
	global range_FR
	global range_F
	global range_FL
	global range_L
	global vel_pub
	global input_vel
	global last_input_vel
	global last_output_vel
	
	ang_correction_vel = 1
	min_fator = 0.3
	
	max_dist = 0.5	# distancia da parede onde a velocidade X comeca a diminuir
	min_dist = 0.15	# distancia da parede onde a velocidade X nao pode ser > 0
	
	output_vel = Twist()
	#fator = 1
	# tratamento da velocidade X
	#if range_F < max_dist and False:
	#	if output_vel.linear.x > 0:
	#		fator = (range_F - min_dist) / (max_dist - min_dist)
	#		if fator < 0:
	#			fator = 0
	#		output_vel.linear.x *= fator
	
	
	a = 0.04877
	b = 0.9512	
	output_vel.linear.x = b * last_output_vel.linear.x + a * last_input_vel.linear.x
	output_vel.angular.z = b * last_output_vel.angular.z + a * last_input_vel.angular.z
		
	if range_L < 0.2:
		output_vel.linear.x = 0;

	vel_pub.publish(output_vel)
	
	last_output_vel = output_vel
	last_input_vel = input_vel
    
def start():
	global vel_pub
    
	rospy.init_node('gate_control')
	rospy.Subscriber('distSensor_R', Range, update_R)
	rospy.Subscriber('distSensor_FR', Range, update_FR)
	rospy.Subscriber('distSensor_F', Range, update_F)
	rospy.Subscriber('distSensor_FL', Range, update_FL)
	rospy.Subscriber('distSensor_L', Range, update_L)
	rospy.Subscriber('cmd_vel_mux/output', Twist, update_vel)
	
	vel_pub = rospy.Publisher('cmd_vel_gate', Twist, queue_size=1)
	
	rate = rospy.Rate(20)
	
	while not rospy.is_shutdown():
		gate_control()
		rate.sleep()

if __name__ == '__main__':
    try:
        start()
    except rospy.ROSInterruptException:
        pass
