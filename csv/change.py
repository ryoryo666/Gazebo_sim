import glob,os
import numpy as np

file_list=glob.glob(os.path.join("", "*.csv"))
file_list.sort()
for i in range(len(file_list)):
	print str(i)+":"+file_list[i]
number=int(raw_input("\nPlot File Number>> "))
data=np.loadtxt(fname=file_list[number], delimiter = ",")
path='../csv/'+file_list[number]

if len(data[0])==6:
	with open(path, mode="w") as f:
		print("Updata Trajectory6")
		for i in range(len(data)):
			a=data[i][5]
			b=data[i][0]
			c=data[i][1]
			d=data[i][2]
			e=data[i][3]
			f=data[i][4]
			buf=str(a)+","+str(b)+","+str(c)+","+str(d)+","+str(e)+","+str(f)+"\n"
			with open(path, mode="a") as f:
				f.write(buf)

elif len(data[0])==5:
	with open(path, mode="w") as f:
		print("Updata Trajectory5")
		t=0.0
		for i in range(len(data)):
			a=t
			b=data[i][0]
			c=data[i][1]
			d=data[i][2]
			e=data[i][3]
			f=data[i][4]
			buf=str(a)+","+str(b)+","+str(c)+","+str(d)+","+str(e)+","+str(f)+"\n"
			with open(path, mode="a") as f:
				f.write(buf)
        	t+=0.01