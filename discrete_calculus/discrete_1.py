import numpy as np 
from matplotlib import pyplot as plt 
import sys

n = int(sys.argv[1])

x = np.linspace(0, 2*np.pi, n + 1)
s = np.sin(x)

plt.plot(x, s, label=f"n = {n}")
plt.legend()
plt.show()
