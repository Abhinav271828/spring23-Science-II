from random import randint
import matplotlib.pyplot as plt
from tqdm import tqdm

s = 100000

a = -5
b = 5

def one_drunk(n):
    pos = a
    success = 0
    for _ in range(s):
        for _ in range(n):
            pos += randint(0,1)*2-1
        if pos == a: success += 1
    return (success/s)

def two_drunk(n):
    pos1 = a
    pos2 = b
    success = 0
    for _ in range(s):
        for _ in range(n):
            pos1 += randint(0,1)*2-1
            pos2 += randint(0,1)*2-1
        if pos1 == pos2: success += 1
    return (success/s)

def mean_disp(n):
    pos = 0
    mean = 0
    for _ in range(s):
        for _ in range(n):
            pos += randint(0,1)*2-1
        mean += abs(pos)
    mean /= s
    return mean

nlist = list(range(1, 101, 5))
one_plist = []
two_plist = []
dlist = []
for n in tqdm(nlist):
    p = one_drunk(n)
    one_plist.append(p)
    p = two_drunk(n)
    two_plist.append(p)
    d = mean_disp(n)
    dlist.append(d)

plt.plot(nlist, one_plist)
plt.show()
plt.plot(nlist, two_plist)
plt.show()
plt.plot(nlist, dlist)
plt.show()
