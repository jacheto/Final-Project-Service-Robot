#!/usr/bin/env python
# -*- coding: UTF-8 -*-
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
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from actionlib_msgs.msg import GoalStatus
from geometry_msgs.msg import PoseStamped
from nav_msgs.msg import Path
import actionlib
from geometry_msgs.msg import Pose, Point, Quaternion
import math
import os

class Point():
	def __init__(self, x = None, y = None, ang = None):
		self.x = x
		self.y = y
		self.ang = ang
	def p(self):
		print("x: " + str(self.x) + " y: " + str(self.y) + " ang: " + str(self.ang*180/np.pi))
	def equals(self, p):
		return self.x == p.x and self.y == p.y and self.ang == p.ang

def sumPoints(p1, p2):
	x = p1.x + p2.x
	y = p1.y + p2.y
	ang = p1.ang + p2.ang
	return Point(x, y, ang)

def subPoints(p1, p2):
	x = p1.x - p2.x
	y = p1.y - p2.y
	ang = p1.ang - p2.ang
	return Point(x, y, ang)


def pintar(img, x, y, color):
	for xp in range(int(x-2), int(x+2)):
		for yp in range(int(y-2), int(y+2)):
			try:
				img[xp, yp, 0] = color[2]
				img[xp, yp, 1] = color[1]
				img[xp, yp, 2] = color[0]
			except:
				pass
	return img

def PaintPoint(img, point, color):
	for xp in range(int(point.x-2), int(point.x+2)):
		for yp in range(int(point.y-2), int(point.y+2)):
			try:
				img[xp, yp, 0] = color[2]
				img[xp, yp, 1] = color[1]
				img[xp, yp, 2] = color[0]
			except:
				pass
	return img

def rotateImage(image, x_center, y_center, angle):
	center = (x_center, y_center)
	rot_mat = cv2.getRotationMatrix2D(center,angle,1.0)
	return cv2.warpAffine(image, rot_mat, image.shape[0:2], flags=cv2.INTER_LINEAR, borderValue=(205, 205, 205))

def relativize_image(from_image, pos_to_px):
	to_img = rotateImage(from_image, pos_to_px.y, pos_to_px.x, -pos_to_px.ang * 180 / np.pi)
	pos_to_px.ang = 0
	return (to_img, pos_to_px)

def transform_point(pos, trans):
	p = Point()
	p.x = pos.x - trans.transform.translation.y / res
	p.y = pos.y + trans.transform.translation.x / res
	p.ang = tf.transformations.euler_from_quaternion([trans.transform.rotation.x,
													trans.transform.rotation.y,	
													trans.transform.rotation.z,	
													trans.transform.rotation.w])[2]
	return p

def back_transform_point(p0, trans_p0_p1, p2_relativo_a_p1):
	p = Point()
	trans_x = trans_p0_p1.transform.translation.x / res
	trans_y = trans_p0_p1.transform.translation.y / res
	trans_ang = tf.transformations.euler_from_quaternion([trans_p0_p1.transform.rotation.x,
														  trans_p0_p1.transform.rotation.y,	
														  trans_p0_p1.transform.rotation.z,	
														  trans_p0_p1.transform.rotation.w])[2]
	S = math.sin(trans_ang)
	C = math.cos(trans_ang)
	p.x = trans_x + C * p2_relativo_a_p1.x - S * p2_relativo_a_p1.y
	p.y = trans_y + S * p2_relativo_a_p1.x + C * p2_relativo_a_p1.y
	p.ang = p2_relativo_a_p1.ang + trans_ang
	p = sumPoints(p0, p)
	return p


def get_res(yaml_path):
    
	yaml_info = None
	if os.path.isfile(yaml_path):
		with open(yaml_path, 'r') as f:
			try:
				yaml_info = yaml.safe_load(f)
			except:
				pass

	if yaml_info is None:
		return None
	
	res = yaml_info['resolution']
	return res

def get_origin(map_img, yaml_path):
	yaml_info = None
	with open(yaml_path, 'r') as f:
		try:
			yaml_info = yaml.safe_load(f)
		except:
			pass

	if yaml_info is None:
		return None
	
	yaml_resolution = yaml_info['resolution']
	
	Origin = Point()
	img_shape = np.shape(map_img)

	Origin.x = int(img_shape[0] + yaml_info['origin'][1] / yaml_resolution)
	Origin.y = int(- yaml_info['origin'][0] / yaml_resolution)
	Origin.ang = yaml_info['origin'][2]
	
	return Origin

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

def update_path(path):
	global pathPoints
	pathPoints = []
	for p in path.poses:
		pathPoints.append(Point(-p.pose.position.y/res, p.pose.position.x/res, 0))

def update_goal(goal):
	global goal_pos
	
	goal_pos = Point(-goal.pose.position.y/res, goal.pose.position.x/res, tf.transformations.euler_from_quaternion([
		goal.pose.orientation.x,
		goal.pose.orientation.y,	
		goal.pose.orientation.z,	
		goal.pose.orientation.w])[2])
	

def loop2():
	global pathPoints
	global AppMsg
	global goal_pos
	global res
	rospy.init_node('tratamento_mapa')
	rospy.Subscriber('appMsgs', AppMsg, update_AppMsg)
	goal_client = actionlib.SimpleActionClient('move_base', MoveBaseAction)
	rate = rospy.Rate(1)

	tfBuffer = tf2_ros.Buffer()
	listener = tf2_ros.TransformListener(tfBuffer)
	map_path = rospy.get_param('~directory') #"/mnt/HD/ROS_maps/roboserv/andar3dnv2"
	map_path_pgm = map_path + '/map_img.pgm'
	costmap_path_pgm = map_path + '/costmap_img.pgm'
	map_path_jpg = map_path + '/map_img.jpg'
	map_path_yaml = map_path + '/map_img.yaml'
	res = get_res(map_path_yaml)
	rospy.Subscriber('/move_base/DWAPlannerROS/global_plan', Path, update_path)
	rospy.Subscriber('/move_base/current_goal', PoseStamped, update_goal)

	pos_odom_px_current_goal = Point(50, 80, 0)

	trans_map_odom = trans_odom_robot = None
	last_pos_goal_px = pos_robot_px_goal = Point()
	pathPoints = []
	goal_pos = Point(0, 0, 0)

	app_screen_w = 368
	app_screen_h = 276
	scale = 0.8
	img_screen_w = app_screen_w * scale
	img_screen_h = app_screen_h * scale
	prop = 0.25

	while not rospy.is_shutdown():
		try:
			trans_map_odom = tfBuffer.lookup_transform('map', 'odom', rospy.Time())
			trans_odom_robot = tfBuffer.lookup_transform('odom', 'base_link', rospy.Time())
		except:
			pass
		
		if trans_map_odom is not None and trans_odom_robot is not None:

			# Obtem a imagem do mapa e sua posicao inicial
			if os.path.isfile(map_path_pgm):
				map_img = cv2.imread(map_path_pgm)
				pos_map_px = get_origin(map_img, map_path_yaml)

				# Obtem a imagem map -> odom e a posicao do odom neste mapa
				pos_odom_px = transform_point(pos_map_px, trans_map_odom)
				(odom_img, pos_odom_px) = relativize_image(map_img, pos_odom_px)

				
				# Pinta o caminho no mapa odom
				for p in pathPoints:
					odom_img = PaintPoint(odom_img, sumPoints(pos_odom_px, p), (0, 255, 0))
				

				# Pinta o current goal no mapa odom
				pos_map_px_current_goal = sumPoints(pos_odom_px, goal_pos)
				odom_img = PaintPoint(odom_img, pos_map_px_current_goal, (0, 0, 255))
				

				# Obtem a imagem odom -> robot e a posicao do robot neste mapa
				pos_robot_px = transform_point(pos_odom_px, trans_odom_robot)
				odom_img = PaintPoint(odom_img, pos_robot_px, (0, 0, 255))
				(robot_img, pos_robot_px) = relativize_image(odom_img, pos_robot_px)
				
				# Pinta o robo no mapa robot
				robot_img = PaintPoint(robot_img, pos_robot_px, (255, 0, 0))
				
				# Corta o mapa robot nas proporcoes que sera enviado para o app
				robot_img_w = np.shape(robot_img)[0]
				robot_img_h = np.shape(robot_img)[1]
				backgroung_img = np.zeros([robot_img_w * 2, robot_img_h * 2, 3], dtype=np.uint8)
				backgroung_img.fill(205)
				backgroung_img[robot_img_w * 1/2: robot_img_w * 3/2, robot_img_h * 1/2: robot_img_h * 3/2] = robot_img
				
				backgroung_img = backgroung_img[
					int(robot_img_w * 1/2 + pos_robot_px.x - img_screen_w):
					int(robot_img_w * 1/2 + pos_robot_px.x + img_screen_w),
					int(robot_img_h * 1/2 + pos_robot_px.y - img_screen_w):
					int(robot_img_h * 1/2 + pos_robot_px.y + img_screen_w)]

				final_img = rotateImage(backgroung_img, img_screen_w, img_screen_w, 90)
				
				final_img = final_img[int(img_screen_w - img_screen_h * (1-prop)):int(img_screen_w + img_screen_h*prop), img_screen_w/2:img_screen_w*3/2]
				
				# Salva o mapa em um arquivo
				cv2.imwrite(map_path_jpg, final_img)

				
				pos_goal_px = Point(AppMsg.robot_pos_x, AppMsg.robot_pos_y, 0)

				if isinstance(pos_goal_px.x, float) and isinstance(pos_goal_px.y, float) and not pos_goal_px.equals(last_pos_goal_px):
					
					x_app_px = app_screen_w * 0.5 - pos_goal_px.x
					y_app_px = app_screen_h * (1 - prop) - pos_goal_px.y
					ang_app_px = np.arctan2(x_app_px, y_app_px)

					pos_robot_px_goal = Point(x_app_px, y_app_px, ang_app_px)
					pos_robot_m_goal = Point(x_app_px * res, y_app_px * res, ang_app_px)
					
					pos_odom_px_goal = back_transform_point(pos_odom_px, trans_odom_robot, pos_robot_px_goal)
					pos_odom_m_goal = Point(pos_odom_px_goal.x*res, pos_odom_px_goal.y*res, pos_odom_px_goal.ang)
					
					if np.sqrt((x_app_px*res) ** 2 + (y_app_px*res) ** 2) > 10:
						print("Escolha um ponto de até 10 m de distância!")
					else:
						
						#pos_odom_px_goal.p()

						(rx, ry, rz, rw) = tf.transformations.quaternion_from_euler(0, 0, ang_app_px)

						goal = MoveBaseGoal()
						goal.target_pose.header.frame_id = "base_link"
						goal.target_pose.header.stamp = rospy.Time.now()
						goal.target_pose.pose.position.x = pos_robot_m_goal.y
						goal.target_pose.pose.position.y = pos_robot_m_goal.x
						goal.target_pose.pose.orientation.x = rx
						goal.target_pose.pose.orientation.y = ry
						goal.target_pose.pose.orientation.z = rz
						goal.target_pose.pose.orientation.w = rw
						goal_client.send_goal(goal)
					
					last_pos_goal_px.x = pos_goal_px.x
					last_pos_goal_px.y = pos_goal_px.y
					last_pos_goal_px.ang = pos_goal_px.ang

		rate.sleep()

def loop():
    
	global AppMsg
	global yaml_resolution

	rospy.init_node('tratamento_mapa')
	rospy.Subscriber('appMsgs', AppMsg, update_AppMsg)
	goal_client = actionlib.SimpleActionClient('move_base', MoveBaseAction)
	
	rate = rospy.Rate(2)

	# definicao de parametros
	tfBuffer = tf2_ros.Buffer()
	listener = tf2_ros.TransformListener(tfBuffer)
	map_path = "/mnt/HD/ROS_maps/roboserv/andar3dnv2"#rospy.get_param('~directory')
	map_path_pgm = map_path + '/map_img.pgm'
	map_path_jpg = map_path + '/map_img.jpg'
	map_path_yaml = map_path + '/map_img.yaml'
	trans = None
	x_abs_px_anterior = 0
	y_abs_px_anterior = 0
	x_current_goal_px = 0
	y_current_goal_px = 0
	x_px = 0
	y_px = 0
	yaml_resolution = 0
	# tamanho da imagem no celular
	screen_w = 368
	screen_h = 276
	scale = 0.8
	img_size_x = sscreen_w * scale
	img_size_y = screen_h * scale
	prop = 0.25 # 0 -> robo sera mostrado em baixo, 1 -> robo sera mostrado em cima
	count = 0
	while not rospy.is_shutdown():
    		
		# obtem a transformacao entre a origem do mapa e a posicao atual do robo
		try:
			trans = tfBuffer.lookup_transform('map', 'base_link', rospy.Time())
		except:
			pass
		try:
			trans_odom = tfBuffer.lookup_transform('map', 'odom', rospy.Time())
		except:
			pass
		
		if not trans is None and os.path.isfile(map_path_pgm):
    		
			# abre o mapa em pgm
			img = cv2.imread(map_path_pgm)
			
			if not img is None:
				# atualiza a posicao do robo em relacao ao mapa
				(x_origin_px, y_origin_px, x_robot_px, y_robot_px, ang) = get_pos(trans, map_path_yaml, np.shape(img))

				# atualiza a posicao do odom em relacao ao mapa
				(x_origin_px, y_origin_px, x_odom_px, y_odom_px, odom_ang) = get_pos(trans, map_path_yaml, np.shape(img))
				
				img_rot = rotateImage(img, y_origin_px, x_origin_px, 90)
				# rotaciona a imagem com o centro na posicao onde o robo esta
				x = x_origin_px - x_robot_px
				y = y_origin_px - y_robot_px

				x_robot_img_px = img_size_y * (1-prop)
				y_robot_img_px = img_size_x * 0.5

				img_rot = pintar(img_rot, x_current_goal_px, y_current_goal_px, (0, 0, 255))

				img_rot = rotateImage(img_rot, y, x, ang)

				img_rot = pintar(img_rot, x, y, (255, 0, 0))
				
				img_rot_w = np.shape(img_rot)[0]
				img_rot_h = np.shape(img_rot)[1]
				img_background = np.zeros([img_rot_w * 2, img_rot_h * 2, 3], dtype=np.uint8)
				img_background.fill(205)
				img_background[img_rot_w * 1/2: img_rot_w * 3/2, img_rot_h * 1/2: img_rot_h * 3/2] = img_rot	

				final_img = img_background[int(img_rot_w/2+x-x_robot_img_px):int(img_rot_w/2+x+img_size_y*prop), int(img_rot_h/2+y-y_robot_img_px):int(img_rot_h/2+y+img_size_x/2)]
				
				final_img = pintar(final_img, img_size_y*(1-prop), img_size_x * 0.5, (0, 255, 0))
				
				# salva a imgagem como jpg
				cv2.imwrite(map_path_jpg, final_img)
		

		x_abs_px = AppMsg.robot_pos_x
		y_abs_px = AppMsg.robot_pos_y
		count = count + 1
		if isinstance(x_abs_px, float) and isinstance(x_abs_px, float) and yaml_resolution != 0:
			if x_abs_px != x_abs_px_anterior or y_abs_px != y_abs_px_anterior:
				
				x_px = y_abs_px * scale
				y_px = x_abs_px * scale

				x_goal_px = x_origin_px - x_px
				y_goal_px = y_origin_px - y_px
				
				x_goal_m = x_goal_px * yaml_resolution
				y_goal_m = y_goal_px * yaml_resolution

				if np.sqrt(x_goal_m ** 2 + y_goal_m ** 2) > 5:
					print("Escolha um ponto de até 5m de distância!")
				
				goal_ang = np.arctan2(x_goal_m, y_goal_m)

				print("ponto: " + str((x_goal_m, y_goal_m, goal_ang*180/np.pi)))
				
				(rx, ry, rz, rw) = tf.transformations.quaternion_from_euler(0, 0, goal_ang)

				goal = MoveBaseGoal()
				goal.target_pose.header.frame_id = "base_link"
				goal.target_pose.header.stamp = rospy.Time.now()
				goal.target_pose.pose.position.x = x_goal_m
				goal.target_pose.pose.position.y = y_goal_m
				goal.target_pose.pose.orientation.x = rx
				goal.target_pose.pose.orientation.y = ry
				goal.target_pose.pose.orientation.z = rz
				goal.target_pose.pose.orientation.w = rw
				goal_client.send_goal(goal) 

				x_current_goal_px = x + x_px - x_robot_img_px
				y_current_goal_px = y + y_px - y_robot_img_px

				x_abs_px_anterior = x_abs_px
				y_abs_px_anterior = y_abs_px
			

		rate.sleep()


if __name__ == '__main__':
    try:
        loop2()
    except rospy.ROSInterruptException:
        pass
