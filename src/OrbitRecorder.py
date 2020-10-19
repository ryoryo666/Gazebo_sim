#! /usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Twist
import os

def Recorder(odom_msg):
    x_ref=odom_msg.pose.pose.position.x
    y_ref=odom_msg.pose.pose.position.y
    theta_ref=odom_msg.pose.pose.orientation.w
    v_ref=odom_msg.twist.twist.linear.x
    w_ref=odom_msg.twist.twist.angular.z
    rospy.loginfo("Odometry: x=%f y=%f θ=%f", x_ref, y_ref, theta_ref)

    buf=str(x_ref)+","+str(y_ref)+","+str(theta_ref)+","+str(v_ref)+","+str(w_ref)+"\n"
    with open(path, mode="a") as f:
        f.write(buf)

def Set():
    Start_check = Twist()
    while(1):
        Start_check = rospy.wait_for_message("/robot_gazebo/diff_drive_controller/cmd_vel", Twist)
        if not Start_check:
            continue
        break
        print("Record Start")

    rospy.Subscriber("/robot_gazebo/diff_drive_controller/odom", Odometry, Recorder)
    rospy.spin()

if __name__=="__main__":
    try:
        rospy.init_node("Orbit_Recorder", anonymous=False)
        path=rospy.get_param('~csv_path','/home/ryo/catkin_ws/src/gazebo_sim/csv/Target_Orbit.csv')
        oddm_msg=Odometry()
#        print(os.getcwd())
        with open(path, mode="w") as f:
            print("New Orbit")
        Set()

    except rospy.ROSInterruptException: pass
