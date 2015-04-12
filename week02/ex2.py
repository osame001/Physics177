import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('velocities.txt')
time = data[:,0]
velocity = data[:,1]

fig = plt.figure()
ax1 = fig.add_subplot(2,1,1)
ax1.plot(time , velocity , marker="o" , linestyle="-" , color="b")

#plt.savefig("ex2.jpeg" , format="jpeg")

a = 0
N = len(data)
print N
h = (time[-1]-time[0])/(N-1)
s = 0.5*(velocity[-1] + velocity[0])

#ax = plt.subplot()

Distance = np.zeros(N)
#s += velocity[a + h*0]

for k in range(0,N-1):
     Distance[k+1] = Distance[k] + 0.5* h * (velocity[a +h*k] + velocity[a+h*(k+1)])
     s += velocity[ a + h*k]
print(h*s)

distance = np.column_stack((time, Distance))
np.savetxt('distanceVStime.txt', distance)

ax2 = fig.add_subplot(2,1,2)

ax2.plot(time , Distance , marker="o" , linestyle="-" , color="r")

#fig.savefig("ex2.jpeg" , format="jpeg")


plt.savefig("ex2.jpeg" , format="jpeg")
