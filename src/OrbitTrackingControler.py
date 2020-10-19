#! /usr/bin/env python
# -*- coding: utf-8 -*-

import math
import rospy
import numpy as np
import roslaunch
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry

def New_cmd(odom_msg):
	global Target_Orbit,num
	# Now Pose
	x_p=odom_msg.pose.pose.position.x
	y_p=odom_msg.pose.pose.position.y
	theta_p=odom_msg.pose.pose.orientation.w

	# Next point on target orbit
	x_r=Target_Orbit[num][0]
	y_r=Target_Orbit[num][1]
	theta_r=Target_Orbit[num][2]
	v_r=Target_Orbit[num][3]
	w_r=Target_Orbit[num][4]

	# Error value
	x_err= (x_r-x_p)*math.cos(theta_p)+(y_r-y_p)*math.sin(theta_p)
	y_err= -(x_r-x_p)*math.sin(theta_p)+(y_r-y_p)*math.cos(theta_p)
	theta_err=theta_r-theta_p

	New_twist.linear.x  = v_r*math.cos(theta_err)+kx*x_err
	New_twist.angular.z = w_r+v_r*(ky*y_err+kth*math.sin(theta_err))
	pub.publish(New_twist)

	num+=1
#	if num==len(Target_Orbit):
#		launch.shutdown()


def Set():
	rospy.init_node("Kanayama_Method_Controller", anonymous=True)
	rospy.Subscriber("/robot_gazebo/diff_drive_controller/odom", Odometry, New_cmd)
	rospy.spin()


if __name__=="__main__":
    try:
		kx=0.1
		ky=0.1
		kth=0.1

		New_twist=Twist()
		Target_Orbit=np.loadtxt(fname="/home/ryo/catkin_ws/src/gazebo_sim/csv/Orbit1.csv", delimiter = ",")
		num=0
		launch="/home/ryo/catkin_ws/src/gazebo_sim/launch/Tracking.launch"
		pub=rospy.Publisher("/robot_gazebo/diff_drive_controller/cmd_vel", Twist, queue_size=2)
		Set()
    except rospy.ROSInterruptException: pass
