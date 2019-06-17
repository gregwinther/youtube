"""
SIR disease model

S' = -beta*S*I
I' = beta*S*I - nu*I
R' = nu*I
"""

import numpy as np
from ODESolver import ForwardEuler
from matplotlib import pyplot as plt

class SIR:
    def __init__(self, nu, beta, S0, I0, R0):
        """
        nu, beta: parameters in the ODE system
        S0, I0, R0: initial values
        """

        if isinstance(nu, (float, int)):
            # Is number?
            self.nu = lambda t: nu 
        elif callable(nu):
            self.nu = nu

        if isinstance(beta, (float, int)):
            self.beta = lambda t: beta 
        elif callable(beta):
            self.beta = beta

        self.initial_conditions = [S0, I0, R0]

    def __call__(self, u, t):

        S, I, _ = u 

        return np.asarray([
            -self.beta(t)*S*I, # Susceptibles
            self.beta(t)*S*I - self.nu(t)*I, # Infected
            self.nu(t)*I # Recovered
        ])

if __name__ == "__main__":

    beta = lambda t: 0.0005 if t <=10 else 0.0001

    sir = SIR(0.1, beta, 1500, 1, 0)
    solver = ForwardEuler(sir)
    solver.set_initial_conditions(sir.initial_conditions)

    time_steps = np.linspace(0, 60, 1001)
    u, t = solver.solve(time_steps)

    plt.plot(t, u[:, 0], label="Susceptible")
    plt.plot(t, u[:, 1], label="Infected")
    plt.plot(t, u[:, 2], label="Recovered")
    plt.legend()
    plt.show()