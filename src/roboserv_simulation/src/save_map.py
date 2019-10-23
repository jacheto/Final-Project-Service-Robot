#!/usr/bin/env python
# Software License Agreement (BSD License)
#
# Copyright (c) 2008, Willow Garage, Inc.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without

import rospy
import subprocess

def loop():
    
	rospy.init_node('save_map')
	rate = rospy.Rate(1)
	
	map_path = rospy.get_param('~directory')
	count = 0
	while not rospy.is_shutdown():
		subprocess.Popen(['rosrun', 'map_server', 'map_saver', '-f', map_path + '/map_img'])#, "map:=/move_base/global_costmap/costmap"])
		count += 1
		if count == 5:
			subprocess.Popen(['rosrun', 'map_server', 'map_saver', '-f', map_path + '/map_img', "map:=/map"])
			count = 0
		rate.sleep()


if __name__ == '__main__':
    try:
        loop()
    except rospy.ROSInterruptException:
        pass
