#! /usr/bin/env python
# -*- coding: utf-8 -*-

import math
import rospy
import numpy as np
import glob,os
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry

kx=0.05
ky=0.07
kth=0.05
num=1
new_twist=Twist()

def New_cmd(odom_msg):
	global Target_Orbit,num
	# Now Pose
	x_p=odom_msg.pose.pose.position.x
	y_p=odom_msg.pose.pose.position.y
	theta_p=odom_msg.pose.pose.orientation.w

	# Refference point on target orbit
	x_r=Target_Trajectory[num][0]
	y_r=Target_Trajectory[num][1]
	theta_r=Target_Trajectory[num][2]
	v_r=Target_Trajectory[num][3]
	w_r=Target_Trajectory[num][4]

	# Error value
	x_err = (x_r-x_p)*math.cos(theta_p)+(y_r-y_p)*math.sin(theta_p)
	y_err = -(x_r-x_p)*math.sin(theta_p)+(y_r-y_p)*math.cos(theta_p)
	theta_err = theta_r-theta_p

	# New Command Value
	new_twist.linear.x  = v_r*math.cos(theta_err)+kx*x_err
	new_twist.angular.z = w_r+v_r*(ky*y_err+kth*math.sin(theta_err))
	pub.publish(new_twist)

	num+=1
#	if num==len(Target_Orbit):



def Set():
	rospy.init_node("Kanayama_Method_Controller", anonymous=True)
	rospy.Subscriber("/robot_gazebo/diff_drive_controller/odom", Odometry, New_cmd)
	rospy.spin()


if __name__=="__main__":
    try:
		file_list=glob.glob(os.path.join("/home/ryo/catkin_ws/src/gazebo_sim/csv", "Target*"))
		file_list.sort()
		for i in range(len(file_list)):
			file_list[i]=file_list[i].replace("/home/ryo/catkin_ws/src/gazebo_sim/csv/", "")
			file_list[i]=file_list[i].replace(".csv", "")
			print(str(i)+": "+file_list[i])
		number=int(raw_input("FileNumber>> "))
		Target_Trajectory=np.loadtxt(fname=file_list[number], delimiter = ",")

		pub=rospy.Publisher("/robot_gazebo/diff_drive_controller/cmd_vel", Twist, queue_size=2)
		Set()

    except rospy.ROSInterruptException: pass
