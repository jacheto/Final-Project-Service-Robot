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

def AtualizarSensores(sensores):
	global sensor_L
	global sensor_F
	global sensor_R

	sensor_L = sensores.SensorL
	sensor_F = sensores.SensorF
	sensor_R = sensores.SensorR

def ProcessarScan(scan):
	r = list(scan.ranges)
	n = rospy.get_param('~hidden_points') # numero de pontos ignorados de ambos os lados
	
	nan = float('nan')
	r = [nan]*n + r[n:len(r)-n] + [nan]*n
	
	output_scan = scan
	output_scan.ranges = tuple(r)
	pubScan.publish(output_scan)

def tratamento_sensores():
	global pubScan

	rospy.init_node('tratamento_scan')
	rospy.Subscriber('scan_input', LaserScan, ProcessarScan)
	pubScan = rospy.Publisher('scan',  LaserScan, queue_size=1)

	rospy.spin()

if __name__ == '__main__':
	try:
		tratamento_sensores()
	except rospy.ROSInterruptException:
		pass
