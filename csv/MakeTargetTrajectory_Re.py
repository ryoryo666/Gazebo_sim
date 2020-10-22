#! /usr/bin/env python
# -*- coding: utf-8 -*-
import os
import math

path='./TargetTrajectory_Re.csv'
with open(path, mode="w") as f:
    print("New Trajectory")
i=0.0
while(i<=9):
    x_ref=i
    y_ref=5*math.sin(i*(math.pi/2))
    theta_ref=0.0
    v_ref=1.0
    w_ref=0.0
        
    buf=str(x_ref)+","+str(y_ref)+","+str(theta_ref)+","+str(v_ref)+","+str(w_ref)+"\n"
    with open(path, mode="a") as f:
        f.write(buf)
    i+=0.01

