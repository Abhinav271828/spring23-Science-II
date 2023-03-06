import numpy as np
import matplotlib.pyplot as plt

def get_M(D):
    M = np.random.normal(0, 1, size=(500, 500))
    for i in range(500):
        M[i,i] = D
        #for j in range(i, 500): M[i,j] = M[j,i]
    return M
 
def plot_eigs(M, D):
    e, _ = np.linalg.eig(M)
    x = [c.real for c in e]
    y = [c.imag for c in e]
    plt.scatter(x,y, label=f"Diagonal {D}")

plt.xlabel("Real")
plt.ylabel("Imaginary")

plot_eigs(get_M(0), 0)
plot_eigs(get_M(1), 1)
plot_eigs(get_M(5), 5)
plot_eigs(get_M(10), 10)
plt.legend()
plt.show()