import matplotlib.pyplot as plt

def get_rands(n):
    i = 1
    a = 106
    c = 1283
    m = 6075
    random_nos = [i]
    for _ in range(n-1):
        i = (a*i + c) % m
        random_nos.append(i)
    return random_nos

random_nos = get_rands(1000)
plt.plot(range(1000), random_nos)
plt.show()

plt.scatter(random_nos[:-1], random_nos[1:])
plt.show()

avgs = []
n_list = [1, 10, 50] + list(range(100, 2001, 100))
for n in n_list:
    random_nos = get_rands(n)
    avg = sum(random_nos)/len(random_nos)
    avgs.append(avg)

plt.plot(n_list, avgs)
plt.show()