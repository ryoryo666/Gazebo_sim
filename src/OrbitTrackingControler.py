#! /usr/bin/env python
# -*- coding: utf-8 -*-

import rospy

def Pub():
    x_r=rospy.get_param("reference_x")
    y_r=rospy.get_param("reference_y")
    vx_r=
    vy_r=

if __name__=="__main__":
    try:
        Pub()
    except rospy.ROSInterruptException: pass
