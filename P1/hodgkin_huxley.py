from math import exp
import numpy as np


def get_alpha_beta(v_rest, vt):
    u = v_rest - vt
    alpha_n = (0.01 * u + 0.1) / (np.exp(1 + 0.1 * u) - 1)
    beta_n = 0.125 * np.exp(u / 80)
    alpha_m = np.divide((0.1 * u + 2.5), (np.exp(2.5 + 0.1 * u) - 1))
    beta_m = 4 * np.exp(u / 18)
    alpha_h = 0.07 * np.exp(u / 20)
    beta_h = np.divide(1.0, (1 + np.exp(3 + 0.1 * u)))
    return alpha_n, beta_n, alpha_m, beta_m, alpha_h, beta_h


def get_tha(v_rest, vt):
    alpha_n, beta_n, alpha_m, beta_m, alpha_h, beta_h = get_alpha_beta(v_rest, vt)
    tha_n = 1.0 / (alpha_n + beta_n)
    tha_m = 1.0 / (alpha_m + beta_m)
    tha_h = 1.0 / (alpha_h + beta_h)
    return tha_n, tha_m, tha_h


def get_mnh_steady_state(v_rest, vt):
    alpha_n, beta_n, alpha_m, beta_m, alpha_h, beta_h = get_alpha_beta(v_rest, vt)
    n = alpha_n / (alpha_n + beta_n)
    m = alpha_m / (alpha_m + beta_m)
    h = alpha_h / (alpha_h + beta_h)
    return n, m, h


def calculate_voltage(v0, I, params):
    v_rest = params['v_rest']
    dt = params['dt']
    duration = params['duration']
    gNa, gK, gL = params["gNa"], params["gK"], params['gL']
    eNa, eK, eL = params["eNa"], params["eK"], params['eL']
    cm = params['cm']
    t = int(duration / dt)
    v, n, m, h = np.zeros(t), np.zeros(t), np.zeros(t), np.zeros(t)
    # computing initial values
    v[0] = v0
    alpha_n, beta_n, alpha_m, beta_m, alpha_h, beta_h = get_alpha_beta(v_rest, v0)
    n0 = alpha_n / (alpha_n + beta_n)
    m0 = alpha_m / (alpha_m + beta_m)
    h0 = alpha_h / (alpha_h + beta_h)
    n[0] = n0
    m[0] = m0
    h[0] = h0
    # main loop of euler method
    for i in range(1, t):
        alpha_n, beta_n, alpha_m, beta_m, alpha_h, beta_h = get_alpha_beta(v_rest, v[i - 1])
        ni = n[i - 1] + dt * (alpha_n * (1 - n[i - 1]) - beta_n * n[i - 1])
        mi = m[i - 1] + dt * (alpha_m * (1 - m[i - 1]) - beta_m * m[i - 1])
        hi = h[i - 1] + dt * (alpha_h * (1 - h[i - 1]) - beta_h * h[i - 1])
        i_na = gNa * (v[i - 1] - eNa) * (m[i - 1] ** 3) * h[i - 1]
        i_k = gK * (v[i - 1] - eK) * (n[i - 1] ** 4)
        i_l = gL * (v[i - 1] - eL)
        vi = v[i - 1] + (dt * (I[i - 1] - i_k - i_na - i_l)) / cm
        n[i] = ni
        m[i] = mi
        h[i] = hi
        v[i] = vi

    return v, n, m, h


def get_firing_rate(v0, I, params, limit=20):
    fires = 0
    v_rest = params['v_rest']
    dt = params['dt']
    duration = params['duration']
    gNa, gK, gL = params["gNa"], params["gK"], params['gL']
    eNa, eK, eL = params["eNa"], params["eK"], params['eL']
    cm = params['cm']
    t = int(duration / dt)
    v, n, m, h = np.zeros(t), np.zeros(t), np.zeros(t), np.zeros(t)
    # computing initial values
    v[0] = v0
    alpha_n, beta_n, alpha_m, beta_m, alpha_h, beta_h = get_alpha_beta(v_rest, v0)
    n0 = alpha_n / (alpha_n + beta_n)
    m0 = alpha_m / (alpha_m + beta_m)
    h0 = alpha_h / (alpha_h + beta_h)
    n[0] = n0
    m[0] = m0
    h[0] = h0
    # main loop of euler method
    for i in range(1, t):
        alpha_n, beta_n, alpha_m, beta_m, alpha_h, beta_h = get_alpha_beta(v_rest, v[i - 1])
        ni = n[i - 1] + dt * (alpha_n * (1 - n[i - 1]) - beta_n * n[i - 1])
        mi = m[i - 1] + dt * (alpha_m * (1 - m[i - 1]) - beta_m * m[i - 1])
        hi = h[i - 1] + dt * (alpha_h * (1 - h[i - 1]) - beta_h * h[i - 1])
        i_na = gNa * (v[i - 1] - eNa) * (m[i - 1] ** 3) * h[i - 1]
        i_k = gK * (v[i - 1] - eK) * (n[i - 1] ** 4)
        i_l = gL * (v[i - 1] - eL)
        vi = v[i - 1] + (dt * (I[i - 1] - i_k - i_na - i_l)) / cm
        n[i] = ni
        m[i] = mi
        h[i] = hi
        v[i] = vi
        if v[i - 1] < limit and v[i] >= limit:
            fires += 1

    return max(fires-1,0) / (duration / 1000.0)
