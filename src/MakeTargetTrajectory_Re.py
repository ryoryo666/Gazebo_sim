#! /usr/bin/env python
# -*- coding: utf-8 -*-
import os
import math

path='/home/ryo/catkin_ws/src/gazebo_sim/csv/TargetTrajectory_Re.csv'
with open(path, mode="w") as f:
    print("New Trajectory")
t=0.0
while(t<=30):
    if t<10:
        


    buf=str(x)+","+str(y)+","+str(theta)+","+str(v)+","+str(w)+","+str(time)+"\n"
    with open(path, mode="a") as f:
        f.write(buf)
    i+=0.01
