# -*- coding: utf-8 -*-

import os
import math

c_path=os.path.dirname(os.path.abspath(__file__))
path=c_path+'/../../csv/ReferenceTrajectory_DFL2.csv'
with open(path, mode="w") as f:
    print("\nCreate New Reference Trajectory\n")

t = 0.0
r = 2

dt = 0.05
<<<<<<< HEAD
while t <= 10.0:
    x = 0.2 * t
    y = 0.0 * t
    vx = 0.4
    vy = 0.0
    ax = 0.0
    ay = 0.0
    t += dt

    buf=str(t)+","+str(x)+","+str(y)+","+str(vx)+","+str(vy)+","+str(ax)+","+str(ay)+"\n"
    with open(path, mode="a") as f:
        f.write(buf)

pre_x = x
pre_y = y
th = math.radians(-90)
while t <= 20.0:
    th += math.radians(0.9)
    x = pre_x + math.cos(th)
    y = 1.0 + math.sin(th)
    vx = 0.0
    vy = 0.4
    ax = 0.0
    ay = 0.0
=======
while t <= 30.0:
>>>>>>> 27e56f1855e9ec716b0238dfb17c27032f2a5b70
    t += dt
    x = r * math.cos((math.pi*t) / 15.0)
    y = r * math.sin((math.pi*t) / 15.0)
    vx = r * (math.pi/15.0) * math.sin((math.pi*t) / 15.0) * -1
    vy = r * (math.pi/15.0) * math.cos((math.pi*t) / 15.0)
    ax = r * (math.pi/15.0)**2 * math.cos((math.pi*t) / 15.0) * -1
    ay = r * (math.pi/15.0)**2 * math.sin((math.pi*t) / 15.0) * -1

    buf=str(t)+","+str(x)+","+str(y)+","+str(vx)+","+str(vy)+","+str(ax)+","+str(ay)+"\n"
    with open(path, mode="a") as f:
        f.write(buf)
