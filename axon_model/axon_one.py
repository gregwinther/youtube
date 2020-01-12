import numpy as np

class Axon:

    def __init__(
        self, 
        V_s = 0.1,
        C = 1e-10,
        R1 = 1e8,
        R2 = 1e6,
        N = 1,
    ):

        self.R1 = R1
        self.R2 = R2
        self.C = C

        self.initial_conditions = np.zeros(N)

        if isinstance(V_s, (int, float)):
            self.V_s = lambda t: V_s
            self.initial_conditions[0] = V_s
        elif callable(V_s):
            self.V_s = V_s
            self.initial_conditions[0] = V_s(0)


    def dV(self, V_left_prev, V_prev):

        I2 = (V_left_prev - V_prev) / self.R2
        I1 = V_prev / self.R1

        dV =(I2 - I1) / self.C

        return dV

    def __call__(self, u, t):
        # u is array of voltages at time t
        new_u = np.zeros_like(u)

        new_u[0] = self.dV(self.V_s(t), u[0])

        for i in range(len(u) - 1):
            new_u[i + 1] += self.dV(u[i], u[i + 1]) 

        return new_u

if __name__ == "__main__":

    import sys 
    sys.path.append("../")
    from ODESolver import ForwardEuler

    axon = Axon(N=100)
    solver = ForwardEuler(axon)
    solver.set_initial_conditions(axon.initial_conditions)

    dt = 1e-6
    T = 1e-2
    num_time_steps = int(T/dt)
    time_steps = np.linspace(0, T, num_time_steps)

    u, t = solver.solve(time_steps)

    from matplotlib import pyplot as plt 
    from matplotlib import cm, colors
    new_cmap = colors.LinearSegmentedColormap.from_list("", cm.get_cmap("Greens")(np.linspace(0.4, 1)))

    for i in range(0, num_time_steps, 1000):
        plt.plot(
            u[i, :],
            label = f"time step = {i}",
            color = new_cmap(i/num_time_steps))

    plt.plot(u[-1, :], label="last time step", color="blue")
    plt.legend()
    plt.show()
