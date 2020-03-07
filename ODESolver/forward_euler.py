import numpy as np


def forward_euler(f, U0, T, n):
    """Solve u' = f(u, t), u(0)=u0 with n steps until T"""
    t = np.zeros(n + 1)
    u = np.zeros(n + 1)
    u[0] = U0
    t[0] = 0
    dt = T / n
    for k in range(n):
        t[k + 1] = t[k] + dt
        u[k + 1] = u[k] + dt * f(u[k], t[k])
    return u, t

if __name__ == "__main__":
    from matplotlib import pyplot as plt 
    def f(u, t):
        return u 

    for n in [5, 10, 20, 100]: 
        u, t = forward_euler(f, U0=1, T=4, n=n)
        plt.plot(t, u, linestyle="dashed", label=f"n={n}")

    t_fine = np.linspace(0, 4, 1001)
    plt.plot(t_fine, np.exp(t_fine), label="Exact")
    plt.legend()
    plt.show()

