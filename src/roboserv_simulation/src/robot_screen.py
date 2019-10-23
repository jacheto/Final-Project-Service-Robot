#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Software License Agreement (BSD License)
#
# Copyright (c) 2008, Willow Garage, Inc.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without

import pygame
from pygame.locals import *
import math
import time
import rospy
from pygame import gfxdraw
from roboserv_description.msg import AppMsg

def update_AppMsg(appmsg):
	global AppMsg
	AppMsg = appmsg

def toggle_fullscreen():
    screen = pygame.display.get_surface()
    tmp = screen.convert()
    caption = pygame.display.get_caption()
    cursor = pygame.mouse.get_cursor()  # Duoas 16-04-2007 
    
    w,h = screen.get_width(),screen.get_height()
    flags = screen.get_flags()
    bits = screen.get_bitsize()
    
    pygame.display.quit()
    pygame.display.init()
    
    screen = pygame.display.set_mode((w,h),flags^FULLSCREEN,bits)
    screen.blit(tmp,(0,0))
    pygame.display.set_caption(*caption)

    pygame.key.set_mods(0) #HACK: work-a-round for a SDL bug??

    pygame.mouse.set_cursor( *cursor )  # Duoas 16-04-2007
    
    return screen

if __name__ == '__main__':
    global AppMsg
    rospy.Subscriber('appMsgs', AppMsg, update_AppMsg)
    rospy.init_node('robot_screen')
    
    SW,SH = 640,480
    screen = pygame.display.set_mode((SW,SH))
    pygame.display.set_caption('this is a test')
    screen = pygame.display.get_surface()
    tmp = screen.convert()
    caption = pygame.display.get_caption()
    cursor = pygame.mouse.get_cursor()  # Duoas 16-04-2007 
    
    w,h = screen.get_width(),screen.get_height()
    flags = screen.get_flags()
    bits = screen.get_bitsize()
    
    pygame.display.quit()
    pygame.display.init()
    
    infoObject = pygame.display.Info()
    (w, h) = (infoObject.current_w, infoObject.current_h)

    screen = pygame.display.set_mode((w,h),flags^FULLSCREEN,bits)
    screen.blit(tmp,(0,0))
    pygame.display.set_caption(*caption)

    pygame.key.set_mods(0) #HACK: work-a-round for a SDL bug??
    pygame.mouse.set_visible(False)
    pygame.mouse.set_cursor( *cursor )  # Duoas 16-04-2007

    _quit = False
    t0 = time.time()
    rate = rospy.Rate(60)

    t_abre = float('inf')
    t_fecha = float('inf')
    navigation_mode_anterior = 0
    last_output = 1
    last_setpoint = 1
    last_t = t0
    while not _quit and not rospy.is_shutdown():
        t1 = time.time()
        t = t1 - t0
        t2 = t1 - last_t
        last_t = t1
        for e in pygame.event.get():
            if e.type is QUIT: _quit = True
            if e.type is KEYDOWN and e.key == K_ESCAPE: _quit = True
        
        screen = pygame.display.get_surface()
        
        setpoint = 0 if AppMsg.navigation_mode > 0 else 1

        circle_radius = 400
        circle_barra_y = 40
        circle_barra_h = 20
        
        robot_head_y = 450
        robot_head_x_center = 280
        robot_head_h = 150

        barra_w = 80
        barra_x_center = 120

        olho_h = 120
        olho_x_center = 200
        
        olho_barra_y = 16

        Ta = 5 # Tempo de assentamento (s)
        e = math.exp(- 4/Ta * (t2))
        output = last_output * e + last_setpoint * (1 - e)
        last_setpoint = setpoint
        last_output = output

        olho_barra_h = 8 + 9 * output

        pygame.draw.circle(screen, (255, 255, 255), (w/2, h/2) , circle_radius)
        for i in range(2*circle_radius/circle_barra_y+2):
            pygame.draw.rect(screen, (0, 0, 0), (w/2-circle_radius, h/2-circle_radius + circle_barra_y/2 + (i-1)*circle_barra_y, 2*circle_radius, circle_barra_h), 0)
        
        pygame.draw.rect(screen, (0, 0, 0), (w/2 - barra_x_center - barra_w/2, robot_head_y, barra_w, h), 0)
        pygame.draw.rect(screen, (0, 0, 0), (w/2 + barra_x_center - barra_w/2, robot_head_y, barra_w, h), 0)

        pygame.draw.circle(screen, (0, 0, 0), (w/2 - robot_head_x_center, robot_head_y), robot_head_h/2)
        pygame.draw.circle(screen, (0, 0, 0), (w/2 + robot_head_x_center, robot_head_y), robot_head_h/2)
        pygame.draw.rect(screen, (0, 0, 0), (w/2 - robot_head_x_center, robot_head_y - robot_head_h/2, 2*robot_head_x_center, robot_head_h) , 0)

        pygame.draw.circle(screen, (255, 255, 255), (w/2 - olho_x_center, robot_head_y), olho_h/2)
        pygame.draw.circle(screen, (255, 255, 255), (w/2 + olho_x_center, robot_head_y), olho_h/2)
        for i in range(olho_h/olho_barra_y+1):
            pygame.draw.rect(screen, (0, 0, 0), (w/2 - olho_x_center - olho_h/2, robot_head_y - olho_h/2 - olho_barra_y/2 + i*olho_barra_y, olho_h, olho_barra_h), 0)
            pygame.draw.rect(screen, (0, 0, 0), (w/2 + olho_x_center - olho_h/2, robot_head_y - olho_h/2 - olho_barra_y/2 + i*olho_barra_y, olho_h, olho_barra_h), 0)

        pygame.display.flip()
        rate.sleep()