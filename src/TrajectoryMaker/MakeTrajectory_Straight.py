# -*- coding: utf-8 -*-

import os
import math

c_path=os.path.dirname(os.path.abspath(__file__))
print c_path
path=c_path+'/../../csv/TargetTrajectory_Straight.csv'
with open(path, mode="w") as f:
    print("Make New Trajectory")

t=0.0
x=0.0
y=0.0
th=0.0
last_th=0.0
v=0.0
w=0.0

for x in range(50+1):
    x=x*0.02
    v=0.5

    buf=str(t)+","+str(x)+","+str(y)+","+str(th)+","+str(v)+","+str(w)+"\n"
    with open(path, mode="a") as f:
        f.write(buf)
