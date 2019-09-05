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
	

def safety_control():
	global range_R
	global range_FR
	global range_F
	global range_FL
	global range_L
	global vel_pub
	rate = rospy.Rate(5)

	move = Twist()
	while not rospy.is_shutdown():
		
		if range_L < 0.3:
			move.angular.z = -1
			vel_pub.publish(move)
		
		if range_R < 0.3:
			move.angular.z = 1
			vel_pub.publish(move)
		
		if range_F < 0.3:
			move.linear.x = 0
			move.angular.z = 1
			vel_pub.publish(move)


		rate.sleep()
    
def start():
	global vel_pub
    
	rospy.init_node('safety_control')
	rospy.Subscriber('distSensor_R', Range, update_R)
	rospy.Subscriber('distSensor_FR', Range, update_FR)
	rospy.Subscriber('distSensor_F', Range, update_F)
	rospy.Subscriber('distSensor_FL', Range, update_FL)
	rospy.Subscriber('distSensor_L', Range, update_L)
	vel_pub= rospy.Publisher('cmd_vel_mux/input/safety_controller', Twist, queue_size=1)
	safety_control()

if __name__ == '__main__':
    try:
        start()
    except rospy.ROSInterruptException:
        pass
