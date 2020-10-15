#! /usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry

def New_cmd(odom):
	x_cmd=
	y_cmd=
	v_cmd=

def Set():
	rospy.init_node("Kanayama_Method_Controller", anonymous=True)
	rospy.Subscriber("/robot_gazebo/diff_drive_controller/odom", Odometry, New_cmd)
	pub=rospy.Publisher("/robot_gazebo/diff_drive_controller/cmd_vel", Twist, queue_size=2)

	rospy.spin()


if __name__=="__main__":
    try:
    	Set()
    except rospy.ROSInterruptException: pass
