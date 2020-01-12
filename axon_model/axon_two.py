import numpy as np 
from matplotlib import pyplot as plt
from axon_one import Axon
import sys 
sys.path.append("../")
from ODESolver import ForwardEuler
from scipy.signal import square

V_s = lambda t: 0.1*np.heaviside(square(t*2*np.pi*200), 1)*np.heaviside(0.01 - t, 1)

dt = 1e-6
T = 0.05
num_time_steps = int(T/dt)
time_steps = np.linspace(0, T, num_time_steps)

axon = Axon(V_s=V_s, N=100)
solver = ForwardEuler(axon)
solver.set_initial_conditions(axon.initial_conditions)

u, t = solver.solve(time_steps)

plt.subplot(211)
plt.plot(t, V_s(t))
plt.title("Input signal")
plt.subplot(212)
plt.plot(t, u[:, -1])
plt.title("Output signal")
plt.show()