# -*- coding: utf-8 -*-

import os
import math

c_path=os.path.dirname(os.path.abspath(__file__))
path=c_path+'/../../csv/ReferenceTrajectory_DFL1.csv'
with open(path, mode="w") as f:
    print("\nCreate New Reference Trajectory\n")

t = 0.0
x = 0.0
y = 0.0

<<<<<<< HEAD
dt = 0.05
while t <= 30.0:
=======
dt = 0.01
while t <= 20.0:
>>>>>>> 27e56f1855e9ec716b0238dfb17c27032f2a5b70
    x = 0.4 * t
    y = 0.0 * t
    vx = 0.4
    vy = 0.0
    ax = 0.0
    ay = 0.0
    t += dt

    buf=str(t)+","+str(x)+","+str(y)+","+str(vx)+","+str(vy)+","+str(ax)+","+str(ay)+"\n"
    with open(path, mode="a") as f:
        f.write(buf)
