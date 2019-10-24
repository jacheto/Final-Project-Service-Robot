#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Software License Agreement (BSD License)
#
# Copyright (c) 2008, Willow Garage, Inc.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without

import rospy
import os
import subprocess

def start():
    rospy.init_node('salvar_rviz')
    directory = rospy.get_param('~directory')
    rate = rospy.Rate(5)
    frontmost = None
    while not rospy.is_shutdown():
        if frontmost is None:
            try:
                frontmost = subprocess.check_output(['xwininfo', '-name', 'rviz_config.rviz - RViz']).decode("utf-8").strip().split('\n')
            except:
                try:
                    frontmost = subprocess.check_output(['xwininfo', '-name', 'rviz_config.rviz* - RViz']).decode("utf-8").strip().split('\n')
                except:
                    return
        if not frontmost is None:
            try:
                window_id = frontmost[0][20:30]
                os.system('import -window_id ' + window_id + ' ' + directory + '/rviz_img.png')
            except:
                frontmost = None
        rate.sleep()

    
if __name__ == '__main__':
    try:
        start()
    except rospy.ROSInterruptException:
        pass
