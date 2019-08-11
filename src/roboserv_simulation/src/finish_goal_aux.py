#!/usr/bin/env python
# Software License Agreement (BSD License)
#
# Copyright (c) 2008, Willow Garage, Inc.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without

import rospy
import tf
import math
from sensor_msgs.msg import Range
from geometry_msgs.msg import Twist
from geometry_msgs.msg import PoseStamped
from move_base_msgs.msg import MoveBaseActionFeedback
from move_base_msgs.msg import MoveBaseActionGoal
from actionlib_msgs.msg import GoalStatusArray
from actionlib_msgs.msg import GoalID

goal_pose = PoseStamped()
fb_pose = PoseStamped()
status = 0

tolerance_dist = 0
tolerance_ang = 0
ang_vel = 0

def record_goal_pos(action_goal):
	global goal_pose
	goal_pose = action_goal.goal.target_pose

def record_fb_pos(action_feedback):
	global fb_pose
	fb_pose = action_feedback.feedback.base_position

def record_status(action_status):
	global status
	length = len(action_status.status_list)
	if length > 0:
		status = action_status.status_list[length-1].status

def get_dist(pose1, pose2):
	return ((pose2.pose.position.x-pose1.pose.position.x)**2+(pose2.pose.position.y-pose1.pose.position.y)**2+(pose2.pose.position.z-pose1.pose.position.z)**2)**0.5

def get_ang(p):
	roll, pitch, angle = tf.transformations.euler_from_quaternion([p.pose.orientation.x, p.pose.orientation.y, p.pose.orientation.z, p.pose.orientation.w])
	return angle

def get_dir(ang_robot, ang_goal):
	dir1 = 1 if ang_goal > ang_robot else -1
	dir2 = 1 if abs(ang_goal - ang_robot) > math.pi else -1
	return -dir1*dir2

def finish_goal_aux():
	
	rate = rospy.Rate(5)
	cancel_msg = GoalID()
	move = Twist()
	
	while not rospy.is_shutdown():
		if status == 1:
			dist_from_goal = get_dist(goal_pose, fb_pose)
			
			if dist_from_goal < tolerance_dist:
				ang_robot = get_ang(fb_pose)
				ang_goal = get_ang(goal_pose)
				
				if abs(ang_robot - ang_goal) < tolerance_ang:
					cancel_pub.publish(cancel_msg)
					move.angular.z = 0
					vel_pub.publish(move)
				else:
					direction = get_dir(ang_robot, ang_goal)
					move.angular.z = ang_vel * direction
					vel_pub.publish(move)
		rate.sleep()
	

def start():
	global cancel_pub
	global vel_pub
	
	global tolerance_dist
	global tolerance_ang
	global ang_vel
	
	tolerance_dist = rospy.get_param('/finish_goal_aux/tolerance_dist', 0.2)
	tolerance_ang = rospy.get_param('/finish_goal_aux/tolerance_ang', 0.2)
	ang_vel = rospy.get_param('/finish_goal_aux/ang_vel', 1)
    
	rospy.init_node('finish_goal_aux')
	rospy.Subscriber('move_base/goal', MoveBaseActionGoal, record_goal_pos)
	rospy.Subscriber('move_base/feedback', MoveBaseActionFeedback, record_fb_pos)
	rospy.Subscriber('move_base/status', GoalStatusArray, record_status)
	
	cancel_pub = rospy.Publisher('move_base/cancel', GoalID, queue_size=1)
	vel_pub = rospy.Publisher('cmd_vel_mux/input/switch', Twist, queue_size=1)
	
	finish_goal_aux()

if __name__ == '__main__':
    try:
        start()
    except rospy.ROSInterruptException:
        pass
