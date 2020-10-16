#! /usr/bin/env python
# -*- coding: utf-8 -*-

import math
import rospy
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry

New_twist=Twist()

def New_cmd(odom):
	# Now Pose
	x_p=odom.pose.pose.position.x
	y_p=odom.pose.pose.position.y
	theta_p=odom.pose.pose.orientation.w

	# Next point on target orbit
	x_r=
	y_r=
	theta_r=

	# Error value
	x_err= (x_r-x_p)*math.cos(theta_p)+(y_r-y_p)*math.sin(theta_p)
	y_err= -(x_r-x_p)*math.sin(theta_p)+(y_r-y_p)*math.cos(theta_p)
	theta_err=theta_r-theta_p


	New_twist.twist.twist.linear.x=
	New_twist.twist.twist.angular.z=


def Set():
	rospy.init_node("Kanayama_Method_Controller", anonymous=True)
	rospy.Subscriber("/robot_gazebo/diff_drive_controller/odom", Odometry, New_cmd)
	pub=rospy.Publisher("/robot_gazebo/diff_drive_controller/cmd_vel", Twist, queue_size=2)

	rospy.spin()


if __name__=="__main__":
    try:
    	Set()
    except rospy.ROSInterruptException: pass
