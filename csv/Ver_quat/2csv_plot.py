import glob,os
import numpy as np
import matplotlib.pyplot as plt

fig, ax=plt.subplots()

file_list_M=glob.glob(os.path.join("", "Mobile*"))
file_list_T=glob.glob(os.path.join("", "Target*"))

file_list_M.sort()
for i in range(len(file_list_M)):
	print str(i)+": "+file_list_M[i]
number1=int(raw_input("File Number1>> "))
data1=np.loadtxt(fname=file_list_M[number1], delimiter = ",")
print ""
file_list_T.sort()
for i in range(len(file_list_T)):
	print str(i)+": "+file_list_T[i]
number2=int(raw_input("File Number2>> "))
data2=np.loadtxt(fname=file_list_T[number2], delimiter = ",")

x1=data1[:,1]
y1=data1[:,2]
x2=data2[:,1]
y2=data2[:,2]

ax.plot(x1,y1,color="green", label=file_list_M[number1].replace(".csv",""))
ax.plot(x2,y2, color="red", label=file_list_T[number2].replace(".csv",""))

# Label Name
ax.set_xlabel("X[m]", fontsize=18)
ax.set_ylabel("Y[m]", fontsize=18)

# x and y Axis Limit
lim=5
ax.set_xlim(-1*lim,lim)
ax.set_ylim(-1*lim,lim)

# Position Adjustment
plt.subplots_adjust(bottom=0.15)
plt.subplots_adjust(left=0.2)

# Label Font Size
ax.tick_params(labelsize=15)

ax.grid()
ax.legend()
plt.show()
