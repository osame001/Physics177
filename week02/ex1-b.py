def f(x):
     return x**0.5
a = 0.
b = 2.
N = 10
h = (b-a)/N
s = f(a)/3 +f(b)/3
for k in range(1,N/2):
    s += f(a + (2*k-1)*h)
for k in range(1 , N/2):
    s += f(a +2*k*h)

print(h*s)

