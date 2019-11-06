import numpy as np 
from matplotlib import pyplot as plt
import sys

n = int(sys.argv[1])

h = 2*np.pi / n
x = np.linspace(0, 2*np.pi, n + 1)
s = np.sin(x)
z = np.zeros((len(s)))

for i in range(len(z) - 1):
    z[i] = (s[i + 1] - s[i]) / h 

z[-1] = (s[-1] - s[-2]) / h

plt.plot(x, z, label="Approx")

xfine = np.linspace(0, 2*np.pi, 1001)
exact = np.cos(xfine)
plt.plot(xfine, exact, label="Exact")
plt.legend()
plt.show()
