#!/usr/bin/env python

import rospy
import pygame
from math import exp
from roboserv_description.msg import AppMsg
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
import numpy

class Point():
	def __init__(self, x = None, y = None, ang = None):
		self.x = x
		self.y = y
		self.ang = ang
	def p(self):
		print("x: " + str(self.x) + " y: " + str(self.y) + " ang: " + str(self.ang*180/np.pi))
	def equals(self, p):
		return self.x == p.x and self.y == p.y and self.ang == p.ang

def loop():

    rate = rospy.Rate(20)
    
    PointsList = [
        Point(-0.916830384892, -0.236819291785),    # perto do poster
        Point(1.8523196839, 2.43201789971),         # perto da tv
        Point(-0.0652114767318, 3.01871753926),     # longe do poster
        Point(0.663393627245, -0.589388137909)      # longe da tv
    ]
    index = 0

    while not rospy.is_shutdown():





        prox_index = (index + 1) % len(PointsList)
        x = PointsList[index].x
        y = PointsList[index].y
        ang = np.arctan2(PointsList[prox_index].x - PointsList[index].x, PointsList[prox_index].y - PointsList[index].y)
        (rx, ry, rz, rw) = tf.transformations.quaternion_from_euler(0, 0, ang)
        goal = MoveBaseGoal()
        goal.target_pose.header.frame_id = "odom"
        goal.target_pose.header.stamp = rospy.Time.now()
        goal.target_pose.pose.position.x = y
        goal.target_pose.pose.position.y = x
        goal.target_pose.pose.orientation.x = rx
        goal.target_pose.pose.orientation.y = ry
        goal.target_pose.pose.orientation.z = rz
        goal.target_pose.pose.orientation.w = rw
        goal_client.send_goal(goal)
        rate.sleep()

def start():
    global vel_pub
    global appMsg_pub

    appMsg_pub = rospy.Publisher('appMsgs', AppMsg, queue_size=1)

    rospy.init_node('nav_autonoma')
    vel_pub = rospy.Publisher('cmd_vel_auto', Twist, queue_size=1)

    loop()

if __name__ == '__main__':
    try:
        start()
    except rospy.ROSInterruptException:
        pass
