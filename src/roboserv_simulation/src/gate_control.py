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
from math import exp

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

def update_F(rng):
	global range_F
	range_F = rng.range

def update_L(rng):
	global range_L
	range_L = rng.range
	
def update_vel(vel):
	global input_vel
	input_vel = vel;

def gate_control():
	global range_R
	global range_F
	global range_L
	global vel_pub
	global input_vel
	global last_input_vel
	global last_output_vel
	
	output_vel = Twist()

	# Para o robo caso o sensor seja ativado
	if range_L < 0.3 or range_F < 0.3 or range_R < 0.3:
		last_input_vel.linear.x = 0
	
	# Aplica a rampa e realimenta os estados
	# Tempo de subida: 	2 s
	# Funcao utilizada: G(z) = a/(z-b)
	#a = 0.2212
	#b = 0.7788
	#output_vel.linear.x = b * last_output_vel.linear.x + a * last_input_vel.linear.x
	#output_vel.angular.z = b * last_output_vel.angular.z + a * last_input_vel.angular.z
	
	Ta = 0.2 # Tempo de assentamento (s)
	Hz = 20.0 # Frequencia de atualizacao
	e = exp(- 4/Ta * 1/Hz)
	output_vel.linear.x = last_output_vel.linear.x * e + last_input_vel.linear.x * (1 - e)
	output_vel.angular.z = last_output_vel.angular.z * e + last_input_vel.angular.z * (1 - e)

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
	vel_pub.publish(gate_vel)
    
def start():
	global vel_pub
    
	rospy.init_node('gate_control')
	rospy.Subscriber('distSensor_R', Range, update_R)
	rospy.Subscriber('distSensor_F', Range, update_F)
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
