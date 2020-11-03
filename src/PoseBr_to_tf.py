#! /usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
import tf
from geometry_msgs.msg import Pose2D
from geometry_msgs.msg import Twist
from two_wheel.msg import curve_data
import SpeedClass
import math

def callback(msg):
    global flag
    TurningData.Direction=msg.Direction
    TurningData.Radius=msg.Radius
    print("Subscribe!")
    flag=True
    if TurningData.Direction=="s":
        flag.data=False
        print("Robot stop")
    elif TurningData.Radius==0:
        print("Straight")
    elif TurningData.Radius != 0:
        print("Curve:R=%f" % TurningData.Radius)
        print("Direction:%s (r:Right l:Left)" %TurningData.Direction)


def pub():
    rospy.init_node("robot_pose_publisher", anonymous=True)
    rospy.Subscriber("turning_info", curve_data, callback)
    br=tf.TransformBroadcaster()

    pose.x=0.0
    pose.y=0.0
    pose.theta=math.radians(90)
    r=rospy.Rate(10)

    D=0.3           # Wheel-center distance
    trans_v=0.5     # Translation speed [m/s]
    t=0.0
    dt=0.1

    while not rospy.is_shutdown():
        t+=dt

        # Straight
        if TurningData.Radius == 0 and flag==True:
            vector.linear.x= trans_v * math.cos(pose.theta)
            vector.linear.y= trans_v * math.sin(pose.theta)

            pose.x = pose.x + vector.linear.x*dt
            pose.y = pose.y + vector.linear.y*dt

        # Curve
        elif TurningData.Radius != 0 and flag==True:
            vec=SpeedClass.VW(TurningData,D,trans_v)
            vector.linear.x= trans_v * math.cos(pose.theta)
            vector.linear.y= trans_v * math.sin(pose.theta)
            vector.angular.z=vec.W()

            pose.x = pose.x + vector.linear.x*dt
            pose.y = pose.y + vector.linear.y*dt
            pose.theta = pose.theta + vector.angular.z*dt

        br.sendTransform((pose.x, pose.y, 0.0), tf.transformations.quaternion_from_euler(0, 0, pose.theta), rospy.Time.now(), "body_link", "base_link")

        r.sleep()

if __name__=="__main__":
    TurningData=curve_data()
    pose=Pose2D()
    vector=Twist()
    flag=False

    try:
        pub()
    except rospy.ROSInterruptException: pass
