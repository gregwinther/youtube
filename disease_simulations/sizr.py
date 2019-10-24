"""
The Zombie Apocaplypse!

S' = sigma - beta*S*Z - delta_S*S
I' = beta*S*Z - rho*I - delta_I*I
Z' = rho*I - alpha*S*Z
R' = delta_S*S + delta_I*I + alpha*S*Z
"""

import numpy as np 
from matplotlib import pyplot as plt
from ODESolver import ForwardEuler

class SIZR:
    def __init__(
        self, sigma, beta, rho, delta_S, delta_I, alpha, S0, I0, Z0, R0
    ):
        """
        The Zombie class

        initial value:  S0, I0, Z0, R0
        """

        for name, argument in locals().items():
            if name not in ('self', 'S0', 'I0', 'R0', 'Z0'):
                if isinstance(argument, (float, int)):
                    setattr(self, name, lambda self, value=argument: value)
                elif callable(argument):
                    setattr(self, name, argument)

        self.initial_conditions = [S0, I0, Z0, R0]

    def __call__(self, u, t):
        """RHS of system of ODEs"""

        S, I, Z, _ = u 

        return np.asarray([
            self.sigma(t) - self.beta(t)*S*Z - self.delta_S(t)*S,
            self.beta(t)*S*Z - self.rho(t)*I - self.delta_I(t)*I,
            self.rho(t)*I - self.alpha(t)*S*Z,
            self.delta_S(t)*S + self.delta_I(t)*I + self.alpha(t)*I 
        ])

if __name__ == "__main__":

    """ The three phases of the Zombie apocaplypse

    Phase 1: initial phase
    Lasts four hours. Some humans meet one zombie.
    sigma = 20, beta = 0.03, rho = 1, S0 = 60, Z0 = 1

    Phase 2: Hysteria
    Lasts 24 hours. Zombie threat is evident.
    beta = 0.0012, alpha = 0.0016, delta_I = 0.014, sigma = 2,
    rho = 1

    Phase 3: Counter-attack
    Lasts five hours.
    alpha = 0.006, beta = 0 (no humans are infected),
    delta_S = 0.007, rho = 1, delta_I = 0.05
    """

    beta = lambda t: 0.03 if t < 4 else (0.0012 if t > 4 and t < 28 else 0)
    alpha = lambda t: 0 if t < 4 else (0.0016 if t > 4 and t < 28 else 0.05)
    sigma = lambda t: 20 if t < 4 else (2 if t > 4 and t < 28  else 0)
    rho = 1
    delta_I = lambda t: 0 if t < 4 else (0.014 if t > 4 and t < 28 else 0.05)
    delta_S = lambda t: 0 if t < 28 else 0.007

    # beta = 0.012
    # alpha = 0.0016
    # sigma = 2
    # rho = 1
    # delta_I = 0.014
    # delta_S = 0.0

    S0 = 60
    I0 = 0
    Z0 = 1
    R0 = 0

    zombie_model = SIZR(
        sigma, beta, rho, delta_S, delta_I, alpha, S0, I0, Z0, R0
    )
    solver = ForwardEuler(zombie_model)
    solver.set_initial_conditions(zombie_model.initial_conditions)
    
    time_steps = np.linspace(0, 33, 1001)
    u, t = solver.solve(time_steps)

    plt.plot(t, u[:, 0], label="Susceptible humans")
    plt.plot(t, u[:, 1], label="Infected humans")
    plt.plot(t, u[:, 2], label="Zombies")
    plt.plot(t, u[:, 3], label="Dead")
    plt.legend()
    plt.show()
