import glob,os
import numpy as np
import matplotlib.pyplot as plt

c_path=os.path.dirname(os.path.abspath(__file__))
file_list=glob.glob(os.path.join(c_path, "*.csv"))
file_list.sort()

for i in range(len(file_list)):
	print str(i)+":"+file_list[i].replace(c_path+"/", "")
number=int(raw_input("\nPlot File Number>> "))
data=np.loadtxt(fname=file_list[number], delimiter = ",")
file_name = file_list[number].replace(c_path+"/", "")

x=data[:,1]
y=data[:,2]


#plt.plot(x,y,color="red", lw="1.0", label=file_name)
plt.scatter(x,y,color="red", lw="0.5", s=0.5, label=file_name)


# Label Name
plt.xlabel("X[m]", fontsize=18)
plt.ylabel("Y[m]", fontsize=18)

# x/y Axis Limit
lim=5
plt.xlim(-1*lim,lim)
plt.ylim(-1*lim,lim)
#plt.ylim(-0.1,0.1)

# Position Adjustment
plt.subplots_adjust(bottom=0.15)
plt.subplots_adjust(left=0.2)

# Label Font Size
plt.tick_params(labelsize=15)

plt.grid()
plt.legend()
plt.show()
