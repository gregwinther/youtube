import numpy as np 
import sys 

def diff(f, x, h):
    return (f(x + h) - f(x)) / float(h)

x = eval(sys.argv[1])
h = eval(sys.argv[2])

approx_deriv = diff(np.sin, x, h)
exact_deriv = np.cos(x)
print(f"The approximated value is: {approx_deriv}")
print(f"The exact value is: {exact_deriv}")
print(f"The error is: {exact_deriv - approx_deriv}")
