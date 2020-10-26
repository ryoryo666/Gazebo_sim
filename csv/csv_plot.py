import glob,os
import numpy as np
import matplotlib.pyplot as plt

file_list=glob.glob(os.path.join("", "*.csv"))
file_list.sort()
for i in range(len(file_list)):
	print(str(i)+": "+file_list[i])
number=int(raw_input("FileNumber>> "))
data=np.loadtxt(fname=file_list[number], delimiter = ",")
x=data[:,0]
y=data[:,1]


plt.plot(x,y,color="red")

# Label Name
plt.xlabel("X[m]", fontsize=18)
plt.ylabel("Y[m]", fontsize=18)

# x/y Axis Limit
lim=10
plt.xlim(-1*lim,lim)
plt.ylim(-1*lim,lim)

# Position Adjustment
plt.subplots_adjust(bottom=0.15)
plt.subplots_adjust(left=0.2)

# Label Font Size
plt.tick_params(labelsize=15)

plt.grid()
plt.legend()
plt.show()
