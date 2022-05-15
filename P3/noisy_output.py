import numpy as np
import matplotlib.pyplot as plt


def compute_cdf(gama, deviation, dv):
    v = gama * np.arange(- deviation, + deviation, dv)
    cdf = 0.5 * (1 + np.tanh(v))
    return cdf


def compute_pdf(gama, deviation, dv):
    cdf = compute_cdf(gama, deviation, dv)
    pdf = np.roll(cdf, 1)
    pdf = cdf - pdf
    pdf[0] = cdf[0]
    return pdf


def calculate_voltage(params, RI, v_peak=40):
    v_rest, v_th = params["v_rest"], params["v_th"]
    tha_m = params["tha_m"]
    dt, duration = params["dt"], params["duration"]
    deviation, dv = params["deviation"], params["dv"]
    gama = params["gama"]
    T = int(duration / dt)
    # generating thresholds and pdf
    v_thresh = np.arange(v_th - deviation, v_th + deviation, dv)
    pdf = compute_pdf(gama, deviation, dv)

    v = np.zeros(T)
    spikes = []
    v[0], v[1] = v_rest, v_rest
    for i in range(1, T):
        threshold = np.random.choice(v_thresh, size=1, p=(pdf / np.sum(pdf)))
        if (v[i - 1] >= threshold):
            spikes.append(v[i - 1])
            v[i - 1] = v_peak
            v[i] = v_rest
        else:
            dv = dt * (v_rest - v[i - 1] + RI[i - 1]) / tha_m
            v[i] = v[i - 1] + dv

    return v,spikes
