#! /usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Twist
import os
import Quat_Euler
import math

pre_vx = 0.0
pre_vy = 0.0
pre_t = 0.0
dt = 0.0

def Recorder(odom_msg):
    global time, pre_vx, pre_vy, pre_t
    x=odom_msg.pose.pose.position.x
    y=odom_msg.pose.pose.position.y
    q=Quat_Euler.Quat_TF(0,0, odom_msg.pose.pose.orientation.z, odom_msg.pose.pose.orientation.w)
    theta_ref=q.Euler_z()
    v_ref=odom_msg.twist.twist.linear.x
    vx = v_ref * math.cos(theta_ref)
    vy = v_ref * math.sin(theta_ref)
    time=odom_msg.header.stamp.secs+(odom_msg.header.stamp.nsecs*(10**-9))
    dt = time - pre_t
    ax = (vx - pre_vx) / dt
    ay = (vy - pre_vy) / dt
    print "Odometry:x={0}   y={1}". format(x, y)

    buf=str(time)+","+str(x)+","+str(y)+","+str(vx)+","+str(vy)+","+str(ax)+","+str(ay)+"\n"
    with open(path, mode="a") as f:
        f.write(buf)

    pre_vx = vx
    pre_vy = vy
    pre_t = time

def Set():
    Start_check = Twist()
    while(1):
        Start_check = rospy.wait_for_message("/robot_gazebo/diff_drive_controller/cmd_vel", Twist)
        if not Start_check:
            continue
        break
        print("Record Start")

    rospy.Subscriber("/possition", Odometry, Recorder)
    rospy.spin()

if __name__=="__main__":
    try:
        rospy.init_node("Trajectory_Recorder", anonymous=False)
        path=rospy.get_param('~csv_path','/home/ryo/catkin_ws/src/gazebo_sim/csv/ReferenceTrajectory_DFL0.csv')
        time=0.0
#        print(os.getcwd())
        with open(path, mode="w") as f:
            print("New Trajectory")
        Set()

    except rospy.ROSInterruptException: pass
