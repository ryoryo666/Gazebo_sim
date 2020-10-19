import glob,os
import numpy as np
import matplotlib.pyplot as plt

print(glob.glob(os.path.join("./", "*.csv")))
filename=raw_input("FileName>> ")+".csv"
data=np.loadtxt(fname=filename, delimiter = ",")
x=data[:,0]
y=data[:,1]
lim=20

plt.plot(x,y,color="red")

plt.xlabel("X[m]", fontsize=18)
plt.ylabel("Y[m]", fontsize=18)
#plt.ylabel("speed [m/s]", fontsize=18)
plt.xlim(-1*lim,lim)
plt.ylim(-1*lim,lim)
plt.subplots_adjust(bottom=0.15)
plt.tick_params(labelsize=15)
plt.grid()
plt.legend()
plt.show()
