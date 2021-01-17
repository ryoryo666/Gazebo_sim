# -*- coding: utf-8 -*-

import os
import math

c_path=os.path.dirname(os.path.abspath(__file__))
path=c_path+'/../../csv/ReferenceTrajectory2.csv'
with open(path, mode="w") as f:
    print("\nCreate New Reference Trajectory\n")

t = 0.0
x = 0.0
y = 0.0
th = 0.0
v = 0.5
w = 0.0

dt = 1.0
i = 0
while t <= 125.0:
    x = 4*math.sin(t/10.0)
    y = 4*math.sin(t/20.0)

    t += dt

    buf=str(t)+","+str(x)+","+str(y)+","+str(th)+","+str(v)+","+str(w)+"\n"
    with open(path, mode="a") as f:
        f.write(buf)
