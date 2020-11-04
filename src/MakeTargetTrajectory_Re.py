#! /usr/bin/env python
# -*- coding: utf-8 -*-
import os
import math
import HermiteCurve

path='../csv/TargetTrajectory_Re.csv'
with open(path, mode="w") as f:
    print("New Trajectory")

x_ref=[0,5]
y_ref=[0,5]
vx_ref=[0,10]
vy_ref=[10,0]
t=0.0

hermite=HermiteCurve.HermiteCurve(x_ref,y_ref,vx_ref,vy_ref)
while(t<=0.5):
	x=hermite.xt(t)
	y=hermite.yt(t)
	theta=
	v=

	t+=0.01
	buf=str(x)+","+str(y)+"\n"
	#buf=str(x)+","+str(y)+","+str(theta)+","+str(v)+","+str(w)+","+str(time)+"\n"
	with open(path, mode="a") as f:
		f.write(buf)

#hermite=HermiteCurve.HermiteCurve(x_ref,y_ref,vx_ref,vy_ref)
#while(t<=1):
#	x=hermite.xt(t)
#	y=hermite.yt(t)
#	t+=0.01
#	buf=str(x)+","+str(y)+"\n"
#	#buf=str(x)+","+str(y)+","+str(theta)+","+str(v)+","+str(w)+","+str(time)+"\n"
#	with open(path, mode="a") as f:
#		f.write(buf)
