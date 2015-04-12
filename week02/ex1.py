#trapezoidal method!
def f(x):
    return x**0.5
N = 10
a = 0.0 
b = 2.0
h = (b-a)/N
s = 0.5*f(a) + 0.5*f(b)
for k in range(1,N): #here k goes from 1 to N-1. not N! cool!
    s += f(a+k*h)
print(h*s)

