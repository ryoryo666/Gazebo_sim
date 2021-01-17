# -*- coding: utf-8 -*-

import os
import math

c_path=os.path.dirname(os.path.abspath(__file__))
path=c_path+'/../../csv/ReferenceTrajectory_DFL2.csv'
with open(path, mode="w") as f:
    print("\nCreate New Reference Trajectory\n")

t = 0.0
x = 0.0
y = 0.0
vx = 0.4   #[m/s]
vy = 0.0   #[m/s]

dt = 0.05
while t <= 15.0:
    x += vx * dt
    y += vy * dt
    t += dt

    buf=str(t)+","+str(x)+","+str(y)+","+str(vx)+","+str(vy)+"\n"
    with open(path, mode="a") as f:
        f.write(buf)
pre_x = x
pre_y = y

vx = 0.3   #[m/s]
vy = 0.2   #[m/s]
while t <= 25.0:
    x += vx * dt
    y += vy * dt
    t += dt

    buf=str(t)+","+str(x)+","+str(y)+","+str(vx)+","+str(vy)+"\n"
    with open(path, mode="a") as f:
        f.write(buf)
