#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
ZetCode wxPython tutorial

In this example we create buttons with standard ids.

author: Jan Bodnar
website: www.zetcode.com
last modified: April 2018
"""

import wx
from geometry_msgs.msg import PoseStamped
from geometry_msgs.msg import Twist
import rospy 
import tf
import json
import os 

class Point(object):
    def __init__(self, name = None, X = None, Y = None):
        self.name = name
        self.X = X
        self.Y = Y

class Example(wx.Frame):
    
    def __init__(self, *args, **kw):
        super(Example, self).__init__(*args, **kw)

        rospy.init_node('gui_node')
        self.mb_pub = rospy.Publisher('move_base_simple/goal', PoseStamped, queue_size=1)
        self.vel_pub = rospy.Publisher('cmd_vel_mux/input/teleop', Twist, queue_size=1)
        self.input_vel = Twist()
        self.lin_vel = 0.2
        self.ang_vel = 0.7

        self.get_point_list()
        self.InitUI()

    def InitUI(self):

        pnl = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)
        
        # Ir para ponto

        self.ID_BTN_IR = 30
        self.ID_BTN_SALVAR = 31
        stX = wx.StaticText(pnl, label='Ponto X')
        self.tcX = wx.TextCtrl(pnl)
        stY = wx.StaticText(pnl, label='Ponto Y')
        self.tcY = wx.TextCtrl(pnl)
        btnIr = wx.Button(pnl, label='Ir', id=self.ID_BTN_IR)
        self.tcSave = wx.TextCtrl(pnl)
        btnSalvar = wx.Button(pnl, label='Salvar', id=self.ID_BTN_SALVAR)

        grid = wx.GridSizer(2, 2)
        grid.Add(stX, 0, wx.TOP | wx.LEFT, 9)
        grid.Add(self.tcX, 0, wx.TOP | wx.RIGHT, 9)
        grid.Add(stY, 0, wx.BOTTOM | wx.LEFT, 9)
        grid.Add(self.tcY, 0, wx.BOTTOM | wx.RIGHT, 9)
        vbox.Add(grid, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)

        hbox = wx.BoxSizer(wx.HORIZONTAL)
        hbox.Add(btnIr, wx.RIGHT)
        hbox.Add(self.tcSave, wx.EXPAND)
        hbox.Add(btnSalvar, wx.LEFT)
        vbox.Add((-1, 10))
        vbox.Add(hbox, flag=wx.LEFT | wx.TOP, border=10)

        self.Bind(wx.EVT_BUTTON, self.onPressGo, id=self.ID_BTN_IR)
        self.Bind(wx.EVT_BUTTON, self.onPressSave, id=self.ID_BTN_SALVAR)

        vbox.Add((-1, 10))
        # Controlar robo
        self.BTN_MOVE_UL = 41
        self.BTN_MOVE_UP = 42
        self.BTN_MOVE_UR = 43
        self.BTN_MOVE_LE = 44
        self.BTN_MOVE_CE = 45
        self.BTN_MOVE_RI = 46
        self.BTN_MOVE_DL = 47
        self.BTN_MOVE_DO = 48
        self.BTN_MOVE_DR = 49

        grid = wx.GridSizer(3, 3)
        grid.AddMany([
            (wx.Button(pnl, label='Frente Esquerda', id=self.BTN_MOVE_UL), 0, wx.EXPAND),
            (wx.Button(pnl, label='Frente', id=self.BTN_MOVE_UP), 0, wx.EXPAND),
            (wx.Button(pnl, label='Frente Direita', id=self.BTN_MOVE_UR), 0, wx.EXPAND),
            (wx.Button(pnl, label='Virar Esquerda', id=self.BTN_MOVE_LE), 0, wx.EXPAND),
            (wx.Button(pnl, label='Parar', id=self.BTN_MOVE_CE), 0, wx.EXPAND),
            (wx.Button(pnl, label='Virar Direita', id=self.BTN_MOVE_RI), 0, wx.EXPAND),
            (wx.Button(pnl, label='Re Esquerda', id=self.BTN_MOVE_DL), 0, wx.EXPAND),
            (wx.Button(pnl, label='Re', id=self.BTN_MOVE_DO), 0, wx.EXPAND),
            (wx.Button(pnl, label='Re Direita', id=self.BTN_MOVE_DR), 0, wx.EXPAND)
        ])
        vbox.Add(grid, proportion=1, flag=wx.EXPAND)

        self.Bind(wx.EVT_BUTTON, self.onPressUL, id=self.BTN_MOVE_UL)
        self.Bind(wx.EVT_BUTTON, self.onPressUP, id=self.BTN_MOVE_UP)
        self.Bind(wx.EVT_BUTTON, self.onPressUR, id=self.BTN_MOVE_UR)
        self.Bind(wx.EVT_BUTTON, self.onPressLE, id=self.BTN_MOVE_LE)
        self.Bind(wx.EVT_BUTTON, self.onPressCE, id=self.BTN_MOVE_CE)
        self.Bind(wx.EVT_BUTTON, self.onPressRI, id=self.BTN_MOVE_RI)
        self.Bind(wx.EVT_BUTTON, self.onPressDL, id=self.BTN_MOVE_DL)
        self.Bind(wx.EVT_BUTTON, self.onPressDO, id=self.BTN_MOVE_DO)
        self.Bind(wx.EVT_BUTTON, self.onPressDR, id=self.BTN_MOVE_DR)



        pnl.SetSizer(vbox)
        self.SetTitle("Standard ids")
        self.Centre()

    def onPressUL(self, event):
        self.input_vel.linear.x = self.lin_vel
        self.input_vel.angular.z = self.ang_vel
        self.vel_pub.publish(self.input_vel)
        print('UL')
        
    def onPressUP(self, event):
        self.input_vel.linear.x = self.lin_vel
        self.input_vel.angular.z = 0
        self.vel_pub.publish(self.input_vel)
        print('UP')
        
    def onPressUR(self, event):
        self.input_vel.linear.x = self.lin_vel
        self.input_vel.angular.z = -self.ang_vel
        self.vel_pub.publish(self.input_vel)
        print('UR')
        
    def onPressLE(self, event):
        self.input_vel.linear.x = 0
        self.input_vel.angular.z = self.ang_vel
        self.vel_pub.publish(self.input_vel)
        print('LE')
        
    def onPressCE(self, event):
        self.input_vel.linear.x = 0
        self.input_vel.angular.z = 0
        self.vel_pub.publish(self.input_vel)
        print('CE')
        
    def onPressRI(self, event):
        self.input_vel.linear.x = 0
        self.input_vel.angular.z = -self.ang_vel
        self.vel_pub.publish(self.input_vel)
        print('RI')
        
    def onPressDL(self, event):
        self.input_vel.linear.x = -self.lin_vel
        self.input_vel.angular.z = self.ang_vel
        self.vel_pub.publish(self.input_vel)
        print('DL')
        
    def onPressDO(self, event):
        self.input_vel.linear.x = -self.lin_vel
        self.input_vel.angular.z = 0
        self.vel_pub.publish(self.input_vel)
        print('DO')
        
    def onPressDR(self, event):
        self.input_vel.linear.x = -self.lin_vel
        self.input_vel.angular.z = -self.ang_velang_vel
        self.vel_pub.publish(self.input_vel)
        print('DR')
        
    
    def onPressSave(self, event):
        nome_ponto = self.tcSave.GetValue()
        pos_X = self.tcX.GetValue()
        pos_Y = self.tcY.GetValue()
        substituiu = False
        for i in range(len(self.points_list)):
            if self.points_list[i].name == nome_ponto:
                self.points_list[i].X = pos_X
                self.points_list[i].Y = pos_Y
                substituiu = True
        if not substituiu:
            self.points_list.append(Point(nome_ponto, pos_X, pos_Y))

        with open(self.points_file, 'w') as f:
            json.dump([point.__dict__ for point in self.points_list], f)

    def get_point_list(self):
        self.points_file = "/mnt/HD/ROS_maps/roboserv/saved_points.txt"
        self.points_list = []
        if os.stat(self.points_file).st_size != 0:
            with open(self.points_file, 'r') as f:
                points_dict = json.load(f)
                for p_dict in points_dict:
                    p_list = Point()
                    p_list.__dict__ = p_dict
                    self.points_list.append(p_list)

    def onPressGo(self, event):
        
        ps = PoseStamped()
        ps.pose.position.x = float(self.tcX.GetValue())
        ps.pose.position.y = float(self.tcY.GetValue())
        ps.pose.orientation.z = tf.transformations.quaternion_from_euler(0, 0, 3.141592/2)
        ps.pose.orientation.w = 1
        ps.header.frame_id = "base_link"
        ps.header.stamp = rospy.Time.now()
        self.mb_pub.publish(ps)


def main():

    app = wx.App()
    ex = Example(None)
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
