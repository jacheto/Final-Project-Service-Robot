#!/usr/bin/env python
# Software License Agreement (BSD License)
#
# Copyright (c) 2008, Willow Garage, Inc.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without

import rospy
from sensor_msgs.msg import LaserScan
from roboserv_description.msg import Sensores

sdv = 3 # size of the dist vector 

global sensor_F
global sensor_L
global sensor_R
global sensor_T

sensor_L = [0] * sdv
sensor_F = [0] * sdv
sensor_R = [0] * sdv
sensor_T = [0] * sdv

def AtualizarSensores(sensores):
	global sensor_F
	global sensor_L
	global sensor_R
	global sensor_T

	sensor_F = sensor_F[1:] + [sensores.SensorF]
	sensor_L = sensor_L[1:] + [sensores.SensorL]
	sensor_R = sensor_R[1:] + [sensores.SensorR]
	sensor_T = sensor_T[1:] + [sensores.SensorT]

def ProcessarScan(scan):
	global sensor_F
	global sensor_L
	global sensor_R
	global sensor_T
	r = list(scan.ranges)
	n_hp = rospy.get_param('~hidden_points') # numero de pontos ignorados de ambos os lados
	n_s = 200 # numero de pontos que representarao os sensores ultrassonicos
	nan = float('nan')
	
	
	min_dist = 0.2

	r_L = [min_dist]*n_s if all(i < min_dist for i in sensor_L) else r[:n_s]
	
	r_F = [min_dist]*n_s if all(i < min_dist for i in sensor_F) else r[(len(r)-n_s)/2:(len(r)+n_s)/2]

	r_R = [min_dist]*n_s if all(i < min_dist for i in sensor_R) else r[len(r)-n_s:]
	
	

	r = [nan]*n_hp + r[n_hp:len(r)-n_hp] + [nan]*n_hp
	#r = r_R + r[n_s:(len(r)-n_s)/2] + r_F + r[(len(r)+n_s)/2:len(r)-n_s] + r_L
	
	
	output_scan = scan
	output_scan.ranges = tuple(r)
	pubScan.publish(output_scan)

def tratamento_sensores():
	global pubScan

	rospy.init_node('tratamento_scan')
	rospy.Subscriber('scan_input', LaserScan, ProcessarScan)
	rospy.Subscriber('distSensors', Sensores, AtualizarSensores)
	pubScan = rospy.Publisher('scan',  LaserScan, queue_size=1)

	rospy.spin()

if __name__ == '__main__':
	try:
		tratamento_sensores()
	except rospy.ROSInterruptException:
		pass
