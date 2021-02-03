import glob,os
import numpy as np
import matplotlib.pyplot as plt

fig, ax=plt.subplots()

c_path=os.path.dirname(os.path.abspath(__file__))
file_list=glob.glob(os.path.join(c_path, "*.csv"))

file_list.sort()
for i in range(len(file_list)):
	print str(i)+": "+file_list[i].replace(c_path+"/", "")
number1=int(raw_input("File Number1>> "))
data1=np.loadtxt(fname=file_list[number1], delimiter = ",")
file_list[number1] = file_list[number1].replace(c_path+"/", "")

print ""
for i in range(len(file_list)):
	print str(i)+": "+file_list[i].replace(c_path+"/", "")
number2=int(raw_input("File Number1>> "))
data2=np.loadtxt(fname=file_list[number2], delimiter = ",")
file_list[number2] = file_list[number2].replace(c_path+"/", "")


x1=data1[:,1]
y1=data1[:,2]
x2=data2[:,1]
y2=data2[:,2]

File1 = file_list[number1].replace(".csv","")
File2 = file_list[number2].replace(".csv","")
ax.plot(x1,y1,color="green", label=File1)
ax.plot(x2,y2,color="red",   label=File2)


# Label Name
ax.set_xlabel("X[m]", fontsize=18)
ax.set_ylabel("Y[m]", fontsize=18)

# x and y Axis Limit
x_lim = 11
y_lim = 0.1
ax.set_xlim(-1*x_lim, x_lim)
ax.set_ylim(-1*y_lim, y_lim)

# Position Adjustment
plt.subplots_adjust(bottom=0.15)
plt.subplots_adjust(left=0.2)

# Label Font Size
ax.tick_params(labelsize=15)

ax.grid()
ax.legend()
plt.show()
