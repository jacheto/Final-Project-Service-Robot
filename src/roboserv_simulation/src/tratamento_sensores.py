#!/usr/bin/env python
# Software License Agreement (BSD License)
#
# Copyright (c) 2008, Willow Garage, Inc.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without

import rospy
from sensor_msgs.msg import Range
from roboserv_description.msg import Sensores

def PublicarSensores(sensor):
	global pubSensor_L
	global pubSensor_F
	global pubSensor_R

	range_L =  Range()
	range_F =  Range()
	range_R =  Range()
	
	range_L.header.frame_id = 'distSensor_L'
	range_F.header.frame_id =  'distSensor_F'
	range_R.header.frame_id =  'distSensor_R'
	
	listSensor = [sensor.SensorL, sensor.SensorF, sensor.SensorR]
	
	listRange = [range_L, range_F, range_R]
	
	for i in range(len(listRange)):
		listRange[i].range = listSensor[i]
		listRange[i].min_range = 0.02
		listRange[i].max_range = 4
		listRange[i].radiation_type = 1
		listRange[i].field_of_view = 0.3
		
	

	range_L.range =  sensor.SensorL
	range_F.range =  sensor.SensorF
	range_R.range =  sensor.SensorR

	pubSensor_L.publish(range_L)
	pubSensor_F.publish(range_F)
	pubSensor_R.publish(range_R)

def tratamento_sensores():
	global pubSensor_L
	global pubSensor_F
	global pubSensor_R

	rospy.init_node('tratamento_sensores')
	rospy.Subscriber('distSensors', Sensores, PublicarSensores)

	pubSensor_L =  rospy.Publisher('distSensor_L',  Range, queue_size=1)
	pubSensor_F =  rospy.Publisher('distSensor_F',  Range, queue_size=1)
	pubSensor_R =  rospy.Publisher('distSensor_R',  Range, queue_size=1)

	rospy.spin()

if __name__ == '__main__':
	try:
		tratamento_sensores()
	except rospy.ROSInterruptException:
		pass
