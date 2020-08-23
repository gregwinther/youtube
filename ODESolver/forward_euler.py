import numpy as np


def forward_euler(f_user, U0, T, n):
    """Solve u' = f(u, t), u(0)=u0 with n steps until T"""
    f = lambda u, t: np.asarray(f_user(u, t))
    t = np.zeros(n + 1)
    if isinstance(U0, (int, float)):
        u = np.zeros(n + 1)
    else:
        neq = len(U0)
        u = np.zeros((n + 1, neq))
    u[0, :] = U0
    t[0] = 0
    dt = T / n
    for k in range(n):
        t[k + 1] = t[k] + dt
        u[k + 1, :] = u[k, :] + dt * f(u[k, :], t[k])
    return u, t


if __name__ == "__main__":
    from matplotlib import pyplot as plt

    def f(u, t):
        return [u[1], -u[0]]

    T = 8 * np.pi
    U0 = [0, 1]
    for n in [200, 500, 1000]:
        u, t = forward_euler(f, U0, T, n)
        plt.plot(t, u[:, 0], linestyle="dashed", label=f"n = {n}")

    plt.plot(t, np.sin(t))
    plt.legend()
    plt.show()
