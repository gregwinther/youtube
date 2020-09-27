import numpy as np


class OscSystem:
    """
    System of eqns:
    du0/dt = u1
    du1/dt = w'' + g - (beta/m)*u1 - (k/m)*u0
    """

    def __init__(self, m, beta, k, g, w):
        self.m, self.beta, self.k, self.g, self.w = m, beta, k, g, w
        self.h = 1e-5

    def __call__(self, u, t):
        u0, u1 = u
        m, beta, k, g, w = self.m, self.beta, self.k, self.g, self.w
        # Use finite difference for w''(t)
        ddw = (w(t + self.h) - 2 * w(t) + w(t - self.h)) / (self.h * self.h)
        return np.array([u1, ddw + g - (beta / m) * u1 - (k / m) * u0])


if __name__ == "__main__":
    from ODESolver import ForwardEuler, RungeKutta4
    from matplotlib import pyplot as plt

    periods = 10
    T = periods * 2 * np.pi
    n = int(1e3)

    def w(t):
        if (t > T // 4) and (t < T // 2):
            return np.cos(t)
        else:
            return 0

    # f = OscSystem(1, 0, 1, 0, lambda t: 0)
    # f = OscSystem(1, 0.1, 1, 0, lambda t: 0)
    f = OscSystem(1, 0.1, 1, 0, w)
    ininital_conditions = [1, 0]

    time_points = np.linspace(0, T, n + 1)

    plt.figure()

    for solver_class in [ForwardEuler, RungeKutta4]:
        solver = solver_class(f)
        solver.set_initial_conditions(ininital_conditions)
        u, t = solver.solve(time_points)

        plt.plot(t, u[:, 0], label=f"{solver_class.__name__}")

        # plt.figure()
        # plt.plot(t, u[:, 0], label="Numerical")
        # plt.plot(t, np.cos(t), label="Exact")
        # plt.legend()
        # plt.title(f"{solver_class.__name__}")

    plt.legend()
    plt.show()
