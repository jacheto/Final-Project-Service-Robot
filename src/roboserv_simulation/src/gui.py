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
import rospy 
import tf

class Example(wx.Frame):
    
    def __init__(self, *args, **kw):
        super(Example, self).__init__(*args, **kw)
        
        rospy.init_node('gui_node')
        self.mb_pub = rospy.Publisher('move_base_simple/goal', PoseStamped, queue_size=1)

        self.InitUI()

    def InitUI(self):
        self.ID_BTN = 30
        pnl = wx.Panel(self)
        
        stX = wx.StaticText(pnl, label='Ponto X')
        self.tcX = wx.TextCtrl(pnl)
        stY = wx.StaticText(pnl, label='Ponto Y')
        self.tcY = wx.TextCtrl(pnl)
        btn = wx.Button(pnl, label='Ir', id=self.ID_BTN)

        grid = wx.GridSizer(2, 2)
        grid.Add(stX, 0, wx.TOP | wx.LEFT, 9)
        grid.Add(self.tcX, 0, wx.TOP | wx.RIGHT, 9)
        grid.Add(stY, 0, wx.BOTTOM | wx.LEFT, 9)
        grid.Add(self.tcY, 0, wx.BOTTOM | wx.RIGHT, 9)


        hbox = wx.BoxSizer(wx.HORIZONTAL)
        hbox.Add(btn)
        
        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.Add(grid, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)
        vbox.Add((-1, 10))
        vbox.Add(hbox, flag=wx.LEFT | wx.TOP, border=10)

        self.Bind(wx.EVT_BUTTON, self.onPressGo, id=self.ID_BTN)

        pnl.SetSizer(vbox)

        self.SetTitle("Standard ids")
        self.Centre()

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
