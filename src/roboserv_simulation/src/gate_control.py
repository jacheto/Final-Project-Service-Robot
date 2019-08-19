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
	

def gate_control(input_vel):
	global range_R
	global range_FR
	global range_F
	global range_FL
	global range_L
	global vel_pub
	
	ang_correction_vel = 1
	min_fator = 0.3
	
	max_dist = 0.5	# distancia da parede onde a velocidade X comeca a diminuir
	min_dist = 0.15	# distancia da parede onde a velocidade X nao pode ser > 0
	
	output_vel = input_vel
	fator = 1
	
	# tratamento da velocidade X
	if range_F < max_dist:
		if output_vel.linear.x > 0:
			fator = (range_F - min_dist) / (max_dist - min_dist)
			if fator < 0:
				fator = 0
			output_vel.linear.x *= fator
	
	
	vel_pub.publish(output_vel)
	
    
def start():
	global vel_pub
    
	rospy.init_node('gate_control')
	rospy.Subscriber('distSensor_R', Range, update_R)
	rospy.Subscriber('distSensor_FR', Range, update_FR)
	rospy.Subscriber('distSensor_F', Range, update_F)
	rospy.Subscriber('distSensor_FL', Range, update_FL)
	rospy.Subscriber('distSensor_L', Range, update_L)
	rospy.Subscriber('cmd_vel_mux/output', Twist, gate_control)
	
	vel_pub = rospy.Publisher('cmd_vel_gate', Twist, queue_size=1)
	rospy.spin()

if __name__ == '__main__':
    try:
        start()
    except rospy.ROSInterruptException:
        pass
