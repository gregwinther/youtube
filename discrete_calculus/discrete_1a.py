import numpy as np 
import sys 

xp = eval(sys.argv[1])
n = int(sys.argv[2])

def S_k(k):
    return s[k] + \
        ((s[k+1] - s[k])/(x[k+1] - x[k])) * (xp - x[k])

h = 2*np.pi / n
x = np.linspace(0, 2*np.pi, n + 1)
s = np.sin(x)
k = int(xp/h)

print(f"Approximation of sin({xp}) = {S_k(k)}")
print(f"Exact value sin({xp}) = {np.sin(xp)}")
print(f"Error: {np.sin(xp) - S_k(k)}")
