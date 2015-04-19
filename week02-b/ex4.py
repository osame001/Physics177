 # calculationg integral I=Sin^2(sqrt(100*x)) usint adaptive trapezoidal

# I should mention that I reduced accuracy from 10^-6 to 10^-5, since my laptop could not process that accuracy!
from numpy import sin, sqrt, abs
def f(x):
    return sin(sqrt(100*x))**2
a = 0.
b = 1.
N = 1
h = (b-a)/N
I = 0.5*h*(f(a)+f(b))
print N , I , "no error"

I2 = 0.5*I
M= 2*N
s = (b-a)/M
for k in range(1,M-1,2):
    I2 += f(a + k*s)
e = (1./3)* abs( I2 - I)
print M , I2 , "error is =" , e

while( e > 10**(-5) ):
    I = I2
    M = 2*M
    s = (b-a)/M
    I2 = 0.5*I2
    for i in range(1, M-1, 2):
         I2 += s* f(a + i*s)
    e = (1./3)*abs(I2-I)
    print M , I2 , "\error is = " , e 
print "end"
print "in 19 steps we get this result"
