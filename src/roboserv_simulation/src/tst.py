#!/usr/bin/env python
# Software License Agreement (BSD License)
#
# Copyright (c) 2008, Willow Garage, Inc.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without

import os

rootdir=  "/media/felipe/DATA/ROS_maps/roboserv"
for subdir, dirs, files in os.walk(rootdir):
    print(dirs[0])