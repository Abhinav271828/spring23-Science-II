from math import cos, pi
from random import randint
import matplotlib.pyplot as plt

def f(x): return (cos(x) - cos(x)**2)

def integrate(n):
    avg = 0
    for i in range(n):
        r = randint(0, n-1)
        x = pi * (- 1/2 + r / (n-1))
        avg += f(x)
    
    avg *= pi / (n-1)

    return avg

print(integrate(100000)) # 0.4306645342878994

nlist = list(range(2, 100003, 1000))
ilist = []
for n in nlist:
    i = integrate(n)
    ilist.append(i)

plt.plot(nlist, ilist)
plt.show()