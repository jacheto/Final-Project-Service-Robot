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
from math import pi

def rotateImage(image, x_center, y_center, angle):
    center = (x_center, y_center)
    rot_mat = cv2.getRotationMatrix2D(center,angle,1.0)
    return cv2.warpAffine(image, rot_mat, image.shape[0:2], flags=cv2.INTER_LINEAR, borderValue=(205, 205, 205))


def get_pos(trans, map_path_yaml, img_shape):
    
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

def loop():
    
	rospy.init_node('transform_map')
	rate = rospy.Rate(2)

	# definicao de parametros
	tfBuffer = tf2_ros.Buffer()
	listener = tf2_ros.TransformListener(tfBuffer)
	map_path = '/media/felipe/DATA/ROS_maps/roboserv/andar3'#rospy.get_param('~directory')
	map_path_pgm = map_path + '/map_img.pgm'
	map_path_jpg = map_path + '/map_img.jpg'
	map_path_yaml = map_path + '/map_img.yaml'
	trans = None
	
	# tamanho da imagem no celular
	img_size_x = 200
	img_size_y = 200
	prop = 0.25 # 0 -> robo sera mostrado em baixo, 1 -> robo sera mostrado em cima
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
				print((x_origin_px, y_origin_px, x_robot_px, y_robot_px, ang))
				img_rot[x, y, 0] = 0
				img_rot[x, y, 1] = 0
				img_rot[x, y, 2] = 255
				#img_rot = rotateImage(img, x, y, ang)
				#print(np.shape(img))
				# corta a imagem para manter o robo no centro e se adequar a tela do app
				
				
				img_rot = img_rot[int(x-img_size_y*(1-prop)):int(x+img_size_y*prop), y-int(img_size_x/2):int(y+img_size_x/2)]

				# salva a imgagem como jpg
				cv2.imwrite(map_path_jpg, img_rot)

		rate.sleep()


if __name__ == '__main__':
    try:
        loop()
    except rospy.ROSInterruptException:
        pass
