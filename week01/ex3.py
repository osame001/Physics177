import numpy as np
import matplotlib.pyplot as plt
import pdb
h = 800 # height in meter

g = 9.81 # gravity aaceleration

#vi = input("enter initial velocity=") #initial velocity

vmin = float(input("enter minimum velocity="))

vmax = float(input("enter maximum velocity=")) 

dx = ( vmax -vmin )/10.

t = np.zeros(10)
vel_vector = vmin +np.arange(10).astype('float') * dx
t = ( vel_vector  +( vel_vector**2 +2*g*h)**0.5)/g
#for i in range(10): 
    #vel_vector[i] = vmin + float(i)*dx
    #t[i] = ( vel_vector[i]  +( vel_vector[i]**2 +2*g*h)**0.5)/g

print "time is=" , t , "for velocity=" , vel_vector


plt.plot(vel_vector , t , marker="o" , linestyle="-" , color="b")
plt.ylabel("time")
plt.xlabel("initial velocity")
plt.title("t=(V_initial +(V_initial**2+2*g*h)**0.5))/g")
plt.savefig("ex3.jpeg" , format="jpeg")
