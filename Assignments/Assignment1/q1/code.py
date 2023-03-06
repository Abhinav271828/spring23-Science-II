import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-1, 1, 101)

t = np.array([-1.0, -0.5, 0.0, 0.5, 1.0])
A = []
for i in t:
    A.append([i**2, i, 1])
A = np.array(A)

y = np.array([1.0, 0.5, 0.0, 0.5, 2.0])

a, _, _, _ = np.linalg.lstsq(A, y, rcond=None)

plt.plot(t, y, 'o', label="Datapoints")
plt.plot(x, a[0]*x**2 + a[1]*x + a[2], 'r', label="Fitted curve")
plt.legend()
plt.show()