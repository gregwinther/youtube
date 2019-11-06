import numpy as np

def trapezoidal(f, a, b, n):
    h = (b - a) / n
    I = f(a) + f(b)

    for i in range(1, n):
        x = a + i*h
        I += 2*f(x)

    I *= h/2
    return I

if __name__ == "__main__":
    a = 0.5
    omega = 1.0

    g = lambda t: -a*np.exp(-a*t)*np.sin(np.pi*omega*t) \
        + np.pi*omega*np.exp(-a*t)*np.cos(np.pi*omega*t)
    G = lambda t: np.exp(-a*t)*np.sin(np.pi*omega*t)

    t1 = 0
    t2 = 4

    exact = G(t2) - G(t1)
    for n in [2, 4, 8, 16, 32, 64, 128, 256, 512]:
        approx = trapezoidal(g, t1, t2, n)
        print(f"n = {n}, approx: {approx}, error: {exact - approx}")
