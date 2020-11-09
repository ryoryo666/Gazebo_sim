#! /usr/bin/env python
# -*- coding: utf-8 -*-

import math
import rospy
import numpy as np
import glob,os
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
import Quat_Euler

#Quat
#kx=0.05
#ky=0.07
#kth=0.05

#Euler
kx=0.05
ky=0.1
kth=0.05

num=1
new_twist=Twist()

def New_cmd(odom_msg):
	global num,stop
	# Now Pose
	x_p=odom_msg.pose.pose.position.x
	y_p=odom_msg.pose.pose.position.y
	q=Quat_Euler.Quat_TF(0,0, odom_msg.pose.pose.orientation.z, odom_msg.pose.pose.orientation.w)
	theta_p=q.Euler_z()
#	theta_p=odom_msg.pose.pose.orientation.w

	x_diff=Target_Trajectory[num][1]-x_p
	y_diff=Target_Trajectory[num][2]-y_p

	if math.sqrt((x_diff**2)+(x_diff**2)) < 0.5:
		num+=1
		if num >= stop:
			rospy.signal_shutdown("Finish")

	# Refference point on target trajectory
	x_r=Target_Trajectory[num][1]
	y_r=Target_Trajectory[num][2]
	theta_r=Target_Trajectory[num][3]
	v_r=Target_Trajectory[num][4]
	w_r=Target_Trajectory[num][5]

	# Error value
	x_err = (x_r-x_p)*math.cos(theta_p)+(y_r-y_p)*math.sin(theta_p)
	y_err = -(x_r-x_p)*math.sin(theta_p)+(y_r-y_p)*math.cos(theta_p)
	theta_err = theta_r-theta_p

	# New Command Value
	new_twist.linear.x  = v_r*math.cos(theta_err)+kx*x_err
	new_twist.angular.z = w_r+v_r*(ky*y_err+kth*math.sin(theta_err))
	pub.publish(new_twist)

def Set():
	rospy.init_node("Kanayama_Method_Controller", disable_signals=True, anonymous=True)
	rospy.Subscriber("/robot_gazebo/diff_drive_controller/odom", Odometry, New_cmd)
	rospy.spin()


if __name__=="__main__":
    try:
		file_list=glob.glob(os.path.join("/home/ryo/catkin_ws/src/gazebo_sim/csv", "Target*"))
		file_list.sort()
		print "\n"
		for i in range(len(file_list)):
			print str(i)+":"+file_list[i].replace("/home/ryo/catkin_ws/src/gazebo_sim/csv/", "")
		number=int(raw_input("\nFileNumber>> "))
		Target_Trajectory=np.loadtxt(file_list[number], delimiter = ",")
		stop=len(Target_Trajectory)

		pub=rospy.Publisher("/robot_gazebo/diff_drive_controller/cmd_vel", Twist, queue_size=2)
		Set()

    except rospy.ROSInterruptException: pass
