# -*- coding: utf-8 -*-

import os
import math

path='/home/ryo/catkin_ws/src/gazebo_sim/csv/TargetTrajectory_Straight.csv'
with open(path, mode="w") as f:
    print("Make New Trajectory")

t=0.0
x=0.0
y=0.0
th=0.0
last_th=0.0
v=0.0
w=0.0

for x in range(100+1):
    x=x*0.1
    v=0.5

    buf=str(t)+","+str(x)+","+str(y)+","+str(th)+","+str(v)+","+str(w)+"\n"
    with open(path, mode="a") as f:
        f.write(buf)
