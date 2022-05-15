import numpy as np

v_spike = 30


def izhikevich_model(v0, I, params):
    dt, duration = params['dt'], params['duration']
    a, b, c, d = params['a'], params['b'], params['c'], params['d']
    t = int(duration / dt)
    v, u = np.zeros(t), np.zeros(t)
    v[0] = v0
    u[0] = b * v[0]
    for i in range(1, t):
        dv = 0.04 * (v[i - 1] ** 2) + 5 * v[i - 1] + 140 - u[i - 1] + I[i - 1]
        du = a * (b * v[i - 1] - u[i - 1])
        v[i] = v[i - 1] + dt * dv
        u[i] = u[i - 1] + dt * du
        if v[i - 1] > v_spike:
            v[i] = c
            u[i] = u[i - 1] + d

    return v,u
