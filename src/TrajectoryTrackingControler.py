#! /usr/bin/env python
# -*- coding: utf-8 -*-

import math
import rospy
import rospkg
import numpy as np
import glob,os
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
import Quat_Euler

kx=0.2
ky=2.0
kth=0.0

x_r = 0.0
y_r = 0.0
t = 1.0

pre_v = 0.0
num=0
new_twist=Twist()

def New_cmd(odom_msg):
	global num,stop, x_r, y_r, pre_Time, t
	# Now Pose
	x_p=odom_msg.pose.pose.position.x
	y_p=odom_msg.pose.pose.position.y
	q=Quat_Euler.Quat_TF(0,0, odom_msg.pose.pose.orientation.z, odom_msg.pose.pose.orientation.w) # クウォータニオン　→　オイラー角
	theta_p=q.Euler_z()	# z軸周りの回転

	now_Time = rospy.Time.now()
	dt = now_Time - pre_Time
	dt = dt.secs + dt.nsecs/(10.0**9.0)
	t += dt

	shutdown()

	# Difference Target and Now Pose
	x_diff=x_r - x_p
	y_diff=y_r - y_p
	diff = math.sqrt((x_diff**2)+(x_diff**2))
#	print "X_diff:{0}	Y_diff:{1}".format(x_diff,y_diff)
	print "Diff:{0}".format(diff)
	if diff < 0.1:
		num+=1
	elif diff < 0.01:
		num += 3

	# Refference point on target trajectory
	x_r=Target_Trajectory[num][1]
	y_r=Target_Trajectory[num][2]
	theta_r=Target_Trajectory[num][3]
	v_r=Target_Trajectory[num][4]
	w_r=Target_Trajectory[num][5]
	print "Xr:{0}	Yr:{1}".format(x_r,y_r)

	# Error value
	x_err = (x_r-x_p)*math.cos(theta_p)+(y_r-y_p)*math.sin(theta_p)
	y_err = -(x_r-x_p)*math.sin(theta_p)+(y_r-y_p)*math.cos(theta_p)
	theta_err = theta_r-theta_p

	# New Command Value
	new_twist.linear.x  = v_r*math.cos(theta_err)+kx*x_err
	new_twist.angular.z = w_r+v_r*(ky*y_err+kth*math.sin(theta_err))
	pub.publish(new_twist)

	pre_Time = now_Time

def Set():
	global pre_Time
	rospy.Subscriber("/possition", Odometry, New_cmd)
	pre_Time = rospy.Time.now()
	rospy.spin()

def shutdown():
	global num,stop
	if t >= 125.0:
			print "\nFinish\n"
			new_twist.linear.x  = 0.0
			new_twist.angular.z = 0.0
			pub.publish(new_twist)
			rospy.signal_shutdown("Finish")

if __name__=="__main__":
    try:
		rospy.init_node("Kanayama_Method_Controller", disable_signals=True, anonymous=True)
		pub=rospy.Publisher("/robot_gazebo/diff_drive_controller/cmd_vel", Twist, queue_size=2)
		rospack=rospkg.RosPack()
		pack_path=rospack.get_path("gazebo_sim")

		file_list=glob.glob(os.path.join(pack_path+"/csv", "Reference*"))
		file_list.sort()
		print "\nSelect Reference Trajectory\n"
		for i in range(len(file_list)):
			print str(i)+":"+file_list[i].replace(pack_path+"/csv/", "")
		number=int(raw_input("\nFileNumber>> "))
		Target_Trajectory=np.loadtxt(file_list[number], delimiter = ",")
		stop=len(Target_Trajectory)
		Set()

    except rospy.ROSInterruptException: pass
