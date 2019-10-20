#!/usr/bin/env python
# Software License Agreement (BSD License)
#
# Copyright (c) 2008, Willow Garage, Inc.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without

import rospy
import cv2
import numpy as np
import subprocess
import tf2_ros
import tf
import yaml
import tf
from roboserv_description.msg import AppMsg
from geometry_msgs.msg import PoseStamped
from math import pi


def pintar(img, x, y, color):
	print(np.shape(img))
	print('pontos:')
	print((x, y))
	for xp in range(int(x-2), int(x+2)):
		for yp in range(int(y-2), int(y+2)):
			img[xp, yp, 0] = color[2]
			img[xp, yp, 1] = color[1]
			img[xp, yp, 2] = color[0]
	return img

def rotateImage(image, x_center, y_center, angle):
    center = (x_center, y_center)
    rot_mat = cv2.getRotationMatrix2D(center,angle,1.0)
    return cv2.warpAffine(image, rot_mat, image.shape[0:2], flags=cv2.INTER_LINEAR, borderValue=(205, 205, 205))


def get_pos(trans, map_path_yaml, img_shape):
	global yaml_resolution

	yaml_info = None
	with open(map_path_yaml, 'r') as stream:
		try:
			yaml_info = yaml.safe_load(stream)
		except:
			pass

	if yaml_info is None:
		return None, None, None
	
	yaml_resolution = yaml_info['resolution']

	x_origin_px = int(img_shape[0]+yaml_info['origin'][1]/yaml_resolution)
	y_origin_px = int(-yaml_info['origin'][0]/yaml_resolution)
	x_robot_px = trans.transform.translation.x / yaml_resolution
	y_robot_px = trans.transform.translation.y / yaml_resolution
	
	rot = trans.transform.rotation

	ang = -180/pi * tf.transformations.euler_from_quaternion([rot.x, rot.y, rot.z, rot.w])[2]
	
	return (x_origin_px, y_origin_px, x_robot_px, y_robot_px, ang)


def update_AppMsg(appmsg):
	global AppMsg
	AppMsg = appmsg

def loop():
    
	global AppMsg
	global goal_pub
	global yaml_resolution

	rospy.init_node('transform_map')
	rospy.Subscriber('appMsgs', AppMsg, update_AppMsg)
	goal_pub = rospy.Publisher('/move_base_simple/goal', PoseStamped, queue_size=1)
	rate = rospy.Rate(2)

	# definicao de parametros
	tfBuffer = tf2_ros.Buffer()
	listener = tf2_ros.TransformListener(tfBuffer)
	map_path = "/mnt/HD/ROS_maps/roboserv/andar2"#rospy.get_param('~directory')
	map_path_pgm = map_path + '/map_img.pgm'
	map_path_jpg = map_path + '/map_img.jpg'
	map_path_yaml = map_path + '/map_img.yaml'
	trans = None
	x_abs_px_anterior = 0
	y_abs_px_anterior = 0
	x_px = 0
	y_px = 0
	# tamanho da imagem no celular
	img_size_x = 185
	img_size_y = 140
	prop = 0.25 # 0 -> robo sera mostrado em baixo, 1 -> robo sera mostrado em cima
	count = 0
	while not rospy.is_shutdown():
    		
		# obtem a transformacao entre a origem do mapa e a posicao atual do robo
		try:
			trans = tfBuffer.lookup_transform('map', 'base_link', rospy.Time())
		except:
			pass
		
		if not trans is None:
    		
			# abre o mapa em pgm
			img = cv2.imread(map_path_pgm)
			
			if not img is None:
				# atualiza a posicao do robo em relacao ao mapa
				(x_origin_px, y_origin_px, x_robot_px, y_robot_px, ang) = get_pos(trans, map_path_yaml, np.shape(img))
				
				img_rot = rotateImage(img, y_origin_px, x_origin_px, 90)
				# rotaciona a imagem com o centro na posicao onde o robo esta
				x = x_origin_px - x_robot_px
				y = y_origin_px - y_robot_px
				img_rot = rotateImage(img_rot, y, x, ang)

				img_rot = pintar(img_rot, x, y, (255, 0, 0))
				
				img_rot = img_rot[int(x-img_size_y*(1-prop)):int(x+img_size_y*prop), y-int(img_size_x/2):int(y+img_size_x/2)]

				img_rot = pintar(img_rot, x_px, y_px, (0, 0, 255))
				
				# salva a imgagem como jpg
				cv2.imwrite(map_path_jpg, img_rot)
		

		x_abs_px = AppMsg.robot_pos_x
		y_abs_px = AppMsg.robot_pos_y
		print("oi"+str(count))
		count = count + 1
		if isinstance(x_abs_px, float) and isinstance(x_abs_px, float):
			if x_abs_px != x_abs_px_anterior or y_abs_px != y_abs_px_anterior:
				screen_w = 368
				screen_h = 276 
				x_px = y_abs_px / 2.0
				y_px = x_abs_px / 2.0
				
				x_robot_px = img_size_y * (1 - prop) - y_abs_px
				y_robot_px = x_abs_px - img_size_x / 2

				x_robot_m = x_robot_px * yaml_resolution
				y_robot_m = y_robot_px * yaml_resolution
				print("FOI O PONTO AQUI")
				ps = PoseStamped()
				goal_ang = 0
				(rx, ry, rz, rw) = tf.transformations.quaternion_from_euler(0, 0, goal_ang)

				ps.pose.position.x = x_robot_m
				ps.pose.position.y = y_robot_m
				ps.pose.orientation.x = rx
				ps.pose.orientation.y = ry
				ps.pose.orientation.z = rz
				ps.pose.orientation.w = rw

				#goal_pub.publish(ps)

				x_abs_px_anterior = x_abs_px
				y_abs_px_anterior = y_abs_px
			

		rate.sleep()


if __name__ == '__main__':
    try:
        loop()
    except rospy.ROSInterruptException:
        pass
