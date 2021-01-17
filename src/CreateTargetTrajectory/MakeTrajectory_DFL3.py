# -*- coding: utf-8 -*-

import os
import math

c_path=os.path.dirname(os.path.abspath(__file__))
path=c_path+'/../../csv/ReferenceTrajectory_DFL3.csv'
with open(path, mode="w") as f:
    print("\nCreate New Reference Trajectory\n")

t = 0.0
x = 0.0
y = 0.0

dt = 0.01
while t <= 125.0:
    x = 4*math.sin(t/10.0)
    y = 4*math.sin(t/20.0)
    vx = 0.4*math.cos(t/10.0)
    vy = 0.2*math.cos(t/20.0)
    ax = -0.04*math.sin(t/10.0)
    ay = -0.01*math.sin(t/20.0)
    t += dt

    buf=str(t)+","+str(x)+","+str(y)+","+str(vx)+","+str(vy)+","+str(ax)+","+str(ay)+"\n"
    with open(path, mode="a") as f:
        f.write(buf)
