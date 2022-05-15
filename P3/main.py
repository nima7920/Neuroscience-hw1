import numpy as np
import noisy_output as no
import matplotlib.pyplot as plt

'''
    Question 1
'''
v_th = -45
dv = 0.01
deviation = 10
gama = 0.5
v = np.arange(v_th - deviation, v_th + deviation, dv)
cdf = no.compute_cdf(gama, deviation, dv)
plt.plot(v, cdf, label="CDF")
plt.legend(loc='best')
plt.savefig("../results/p3-cdf.jpg")
plt.show()

pdf = no.compute_pdf(gama, deviation, dv)
plt.plot(v, pdf, label="PDF")
plt.legend(loc='best')
plt.savefig("../results/p3-pdf.jpg")
plt.show()

''' 
    Question 2
'''
v_rest = -70
dt = 0.01
duration = 20
T = int(duration / dt)
t = np.arange(0, duration, dt)
tha_m = 2
RI = 20 * np.ones(T)
params = {
    "v_rest": v_rest,
    "v_th": v_th,
    "RI": RI,
    "dt": dt,
    "duration": duration,
    "tha_m": tha_m,
    "deviation": deviation,
    "dv": dv,
    "gama": gama
}
v, spikes = no.calculate_voltage(params, RI)
plt.plot(t, v)
plt.savefig("../results/p3-noisy output model.jpg")
plt.show()

# plotting voltage for different values of RI
plt.subplot(2, 2, 1)
RI = 20 * np.ones(T)
v, spikes = no.calculate_voltage(params, RI)
plt.title("RI=20")
plt.plot(t, v)

plt.subplot(2, 2, 2)
RI = 30 * np.ones(T)
v, spikes = no.calculate_voltage(params, RI)
plt.title("RI=30")
plt.plot(t, v)

plt.subplot(2, 2, 3)
RI = 40 * np.ones(T)
v, spikes = no.calculate_voltage(params, RI)
plt.title("RI=40")
plt.plot(t, v)

plt.subplot(2, 2, 4)
RI = 50 * np.ones(T)
v, spikes = no.calculate_voltage(params, RI)
plt.title("RI=50")
plt.plot(t, v)
plt.savefig("../results/p3-noisy for RI's.jpg")
plt.show()

''' 
    Question 3
'''
duration = 400
params["duration"] = 400
T = int(duration / dt)
RI = 50 * np.ones(T)
v, spikes = no.calculate_voltage(params, RI)
plt.hist(spikes, bins=50)
plt.savefig("../results/p3-histogram.jpg")
plt.show()

''' 
    Question 4
'''
duration = 100
params["duration"] = 100
i_values = np.arange(0, 60, 1)
firing_rate = np.zeros(60)
T = int(duration / dt)
for i in range(60):
    RI = i * np.ones(T)
    v, spikes = no.calculate_voltage(params, RI)
    firing_rate[i] = len(spikes) / (duration / 1000)

plt.plot(i_values, firing_rate)
plt.savefig("../results/p3-firing rate.jpg")
plt.show()
