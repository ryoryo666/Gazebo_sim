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

# Parameter
kx1 = 2.0   # P gain
ky1 = 2.0
kx2 = 0.5   # D gain
ky2 = 0.5

pre_x = 0.0
pre_y = 0.0
pre_v = 0.0
pre_vx_r = 0.0
pre_vy_r = 0.0
qe = 0.118
uv = 0.0
uw = 0.0
v_max = 0.4
w_max = 0.4

num = 1
new_twist=Twist()

def New_cmd(odom_msg):
    global num, stop, pre_Time, pre_vx_r, pre_vy_r, pre_x, pre_y,t
    global v_max, w_max, uv, uw, qe
	# Now Pose
    x_p = odom_msg.pose.pose.position.x
    y_p = odom_msg.pose.pose.position.y
    # クウォータニオン　→　オイラー角
    q=Quat_Euler.Quat_TF(0,0, odom_msg.pose.pose.orientation.z, odom_msg.pose.pose.orientation.w)
    theta_p=q.Euler_z()	# z軸周りの回転
    v_p = odom_msg.twist.twist.linear.x

#    now_Time = rospy.Time.now()
#    dt = now_Time - pre_Time
#    dt = dt.secs + dt.nsecs/(10.0**9.0)
#    t += dt

    num += 2
    if abs(uv) < 1.0:
        num += 2
    shutdown()

	# Reference point on Reference Path
    x_r = Reference_Path[num][1]
    y_r = Reference_Path[num][2]
    vx_r = Reference_Path[num][3]
    vy_r = Reference_Path[num][4]
    ax_r = Reference_Path[num][5]
    ay_r = Reference_Path[num][6]
#    print "Xr:{0}    Yr:{1}".format(x_r,y_r)
#    print "Vxr:{0}    Vyr:{1}".format(vx_r,vy_r)

	# Error value
    x_err = x_r - x_p
    y_err = y_r - y_p
    vx_err = vx_r - (v_p*math.cos(theta_p))
    vy_err = vy_r - (v_p*math.sin(theta_p))
    print "Xerr:{0}    Yerr:{1}".format(x_err,y_err)

    ux = ax_r + kx1*vx_err + kx2*x_err
    uy = ay_r + ky1*vy_err + ky2*y_err
#    print "ux:{0}    uy:{1}".format(ux,uy)

    qe += ux*math.cos(theta_p) + uy*math.sin(theta_p)
    uv = qe
    uw = ( uy*math.cos(theta_p) - ux*math.sin(theta_p) ) / uv
#    print "uv:{0}    uw:{1}".format(uv,uw)

    z = max([abs(uv)/v_max, abs(uw)/w_max, 1])
    if z == 1:
        Vc = uv
        Wc = uw
    elif z == abs(uv)/v_max:
        Vc = np.sign(uv) * v_max
        Wc = uw / z
    else:
        Vc = uv / z
        Wc = np.sign(uw) * w_max

	# New Command Value
    new_twist.linear.x  = Vc
    new_twist.angular.z = Wc
    pub.publish(new_twist)
#    print "v:{0}    w:{1}".format(Vc,Wc)

    pre_x = x_p
    pre_y = y_p
    pre_v = v_p
    pre_vx_r = vx_r
    pre_vy_r = vy_r
#    pre_Time = now_Time

def Set():
    global pre_Time
    rospy.Subscriber("/possition", Odometry, New_cmd)
#    pre_Time = rospy.Time.now()
    rospy.spin()

def shutdown():
	global num,stop
	if num >= stop:
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
        pack=rospack.get_path("gazebo_sim")
        file_list=glob.glob(os.path.join(pack+"/csv", "Reference*"))
        file_list.sort()
        print "\nSelect Reference Trajectory\n"
        for i in range(len(file_list)):
            print str(i)+":"+file_list[i].replace(pack+"/csv/", "")
        number=int(raw_input("\nFileNumber>> "))
        Reference_Path=np.loadtxt(file_list[number], delimiter = ",")
        stop=len(Reference_Path)

        Set()

    except rospy.ROSInterruptException: pass
