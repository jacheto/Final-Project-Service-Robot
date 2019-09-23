#!/usr/bin/env python
# Software License Agreement (BSD License)
#
# Copyright (c) 2008, Willow Garage, Inc.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without

import rospy
import pygame
from geometry_msgs.msg import Twist
from math import exp

def control():
    global last_input_vel
    global last_output_vel

    last_input_vel = Twist()
    last_output_vel = Twist()

    last_lin_vel = 0
    last_ang_vel = 0

    pygame.init()
    screen_w, screen_h = 640, 480
    screen = pygame.display.set_mode((screen_w, screen_h))
    clock = pygame.time.Clock()

    robot_lin_acel = 0.2
    robot_ang_acel = 0.4

    robot_lin_vel = 0.2
    robot_ang_vel = 1

    robot_lin_stop_time = 2
    robot_ang_stop_time = 1.5

    Hz = 20
    x_vel = 0
    ang_vel = 0

    pygame.draw.line(screen, (255, 255, 255), (0, screen_h/3), (screen_w, screen_h/3), 1)
    pygame.draw.line(screen, (255, 255, 255), (0, screen_h/3*2), (screen_w, screen_h/3*2), 1)
    pygame.draw.line(screen, (255, 255, 255), (screen_w/3, 0), (screen_w/3, screen_h), 1)
    pygame.draw.line(screen, (255, 255, 255), (screen_w/3*2, 0), (screen_w/3*2, screen_h), 1)
    pygame.display.flip()
    
    rate = rospy.Rate(Hz)
    vel = Twist()
    mouse_down = False
    stop = False
    while not rospy.is_shutdown():
        lin_acel = 0
        ang_acel = 0
        lin_stop_time = robot_lin_stop_time
        ang_stop_time = robot_ang_stop_time

        pressed = pygame.key.get_pressed()
        mouse_pos = (screen_w/2, screen_h/2)
        # alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        # ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]
        
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_i:
                    lin_acel += 1
                elif event.key == pygame.K_COMMA:
                    lin_acel += -1

                elif event.key == pygame.K_l:
                    ang_acel += 1
                elif event.key == pygame.K_j:
                    ang_acel += -1
                
                elif event.key == pygame.K_k:
                    lin_acel = 0
                    ang_acel = 0
                    lin_stop_time = 1
                    ang_stop_time = 1
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: # left click grows radius
                    mouse_down = True
                if event.button == 3: # right click shrinks radius
                    stop = True
            if event.type == pygame.MOUSEBUTTONUP:
                stop = False
                mouse_down = False
        
        if mouse_down:
            mouse_pos = event.pos
        
        trans_pos = (-round(float(mouse_pos[0] - screen_w/2)/(screen_w/2),3), -round(float(mouse_pos[1] - screen_h/2)/(screen_h/2),3))
        
        input_vel = Twist()
        output_vel = Twist()

        input_vel.linear.x = trans_pos[1] * 0.3
        input_vel.angular.z = trans_pos[0] * 1.0

        Ta = 2 # Tempo de assentamento (s)
        e = exp(- 4/Ta * 1/Hz)
        output_vel.linear.x = last_output_vel.linear.x * e + last_input_vel.linear.x * (1 - e)
        output_vel.angular.z = last_output_vel.angular.z * e + last_input_vel.angular.z * (1 - e)
        last_output_vel = output_vel
        last_input_vel = input_vel
        print(stop)

        if abs(output_vel.linear.x) > 1e-3 or abs(output_vel.angular.z) > 1e-3:
            if stop:
                output_vel.linear.x = 0
                output_vel.angular.z = 0
            
            vel_pub.publish(output_vel)
        rate.sleep()

def start():
	global vel_pub
    
	rospy.init_node('control_robot')
	vel_pub = rospy.Publisher('cmd_vel_mux/input/teleop', Twist, queue_size=1)
	
	control()

if __name__ == '__main__':
    try:
        start()
    except rospy.ROSInterruptException:
        pass
