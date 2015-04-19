#### calculation of an integral using Trapezoidal and Simpson Method ####

### Trapezoidal Rule ###
  
import numpy as np

from scipy import integrate

def f(x):
    return x**4-2*x+1
a = 0.
b = 2.
N = 20
dx = (b-a)/N 

Res = 0.5*f(a) + 0.5*f(b)

for i in range(1, N):
    Res += f(a +i*dx)

print  "Result using trapezoidal method is="   ,  dx*Res 

### Simpson Rule ###

Res2 = f(a) +f(b)

for i in range(1 , N , 2):
    Res2 += 4*f(a + i*dx)
for j in range(2 , N-1 , 2):
     Res2 += 2*f(a + j*dx)

print "Result using simpson method is=" , (1./3)*dx* Res2

### using scipy ###

s = np.linspace(0 , 2 ,num= 20)

t = np.linspace(0 , 2 ,num= 10)

y = f(s)

g = f(t)

I1 = integrate.trapz(y , s)

I2 = integrate.trapz(g , t)

e1 = (1./3)*(I2-I1)

I3 = integrate.simps(y ,s)

I4 = integrate.simps(g , t)

e2 = (1./15)*(I4-I3)

print "Result using scipy.trapz with N=10 is =" , I2
print "Result using scipy.trapz with N=20 is =" , I1 

print "Error between N=10 and N=20 with scipy.trapz is=" , e1

print "Result using scipy.trapz with N=10 is =" , I4
print "Result using scipy.trapz with N=20 is =" , I3

print "Error between N=10 and N=20 with scipy.simps is=" , e2

Real = 4.4

print "Real value of this integral is=" , Real

