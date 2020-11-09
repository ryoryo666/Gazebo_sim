#! /usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from geometry_msgs.msg import Twist

def Pub():
    rospy.init_node("test_pub", disable_signals=True)
    pub=rospy.Publisher("/robot_gazebo/diff_drive_controller/cmd_vel", Twist, queue_size=2)
    twist=Twist()
    count=0.0
    r=rospy.Rate(20)

    while not rospy.is_shutdown():
        if count <= 2.0:
            twist.linear.x=1.0
            twist.angular.z=-0.0
        elif count <= 15.0:
            twist.linear.x=1.0
            twist.angular.z=-0.5
        elif count <= 27:
            twist.linear.x=1.0
            twist.angular.z=--0.5
        elif count <= 30.0:
            twist.linear.x=1.0
            twist.angular.z=0.0
        else:
            break

        pub.publish(twist)
        count+=0.05
        r.sleep()

    rospy.signal_shutdown("Finish")

if __name__=="__main__":
    try:
        Pub()
    except rospy.ROSInterruptException: pass
