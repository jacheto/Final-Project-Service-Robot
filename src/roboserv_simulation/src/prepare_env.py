#!/usr/bin/env python
# Software License Agreement (BSD License)
#
# Copyright (c) 2008, Willow Garage, Inc.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without

import rospy
import os

def inicializar():
    rospy.init_node('prepare_env')
    directory = rospy.get_param('~directory')
    if not os.path.isdir(directory):
        os.mkdir(directory)

if __name__ == '__main__':
	try:
		inicializar()
	except rospy.ROSInterruptException:
		pass
