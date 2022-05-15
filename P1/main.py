import math
from scipy.signal import chirp, sawtooth
import numpy as np
import matplotlib.pyplot as plt
import hodgkin_huxley as hh

''' Initializing constants '''
v_rest = -60
dt = 0.01
duration = 100
T = int(duration / dt)
t = np.arange(0, T) * dt

params = {
    "dt": dt,
    "duration": duration,
    "v_rest": -60,
    "cm": 1,
    "gNa": 120,
    "gK": 36,
    "gL": 0.3,
    "eNa": 55,
    "eK": -72,
    "eL": -49.4
}
'''  
  Question 1 
'''
v = np.arange(-80, 20, 0.03)
n, m, h = hh.get_mnh_steady_state(v_rest, v)
plt.plot(v, n, label='n')
plt.plot(v, m, label='m')
plt.plot(v, h, label='h')
plt.legend(loc='best')
plt.xlabel("vt")
plt.savefig("../results/p1-mnh-steady.jpg")
plt.show()

tha_n, tha_m, tha_h = hh.get_tha(v_rest, v)
plt.plot(v, tha_n, label='tha_n')
plt.plot(v, tha_m, label='tha_m')
plt.plot(v, tha_h, label='tha_h')
plt.legend(loc='best')
plt.xlabel("vt")
plt.savefig("../results/p1-tha.jpg")
plt.show()

'''
    Question 2
'''
I = np.zeros(T)
I[500:] = 10
v, n, m, h = hh.calculate_voltage(v_rest, I, params)
plt.plot(t, v)
plt.ylabel("v")
plt.savefig("../results/p1-voltage plot.jpg")
plt.show()

''' 
    Question 3
'''
# minimum external current for spiking is 6.21 mA
c = 6.21
I[500:] = c
v, n, m, h = hh.calculate_voltage(v_rest, I, params)
plt.plot(t, v)
plt.ylabel("v")
plt.savefig("../results/p1-voltage plot for minimum current (6.21).jpg")
plt.show()

''' 
    Question 4
'''
c = 6.21
I = np.zeros(T)
I[1000:3020] = c
v, n, m, h = hh.calculate_voltage(v_rest, I, params)
plt.plot(t, v)
plt.ylabel("v")
# plt.savefig("../results/p1-voltage plot for minimum current (6.21).jpg")
plt.show()

'''  
    Question 6 
'''

'''  Question 7 '''
I = np.arange(0, 200, 200.0 / T)
v, n, m, h = hh.calculate_voltage(v_rest, I, params)
plt.subplot(2, 1, 1)
plt.ylabel("V")
plt.plot(t, v)
plt.subplot(2, 1, 2)
plt.ylabel("I")
plt.plot(t, I, color="red")
plt.savefig("../results/p1-q7 varying current")
plt.show()

''' Question 8 '''
# small current
I = np.ones(T) * 5
v, n, m, h = hh.calculate_voltage(v_rest, I, params)

plt.plot(t, v)
plt.savefig("../results/p1-q8 small current.jpg")
plt.show()
plt.plot(v, n, label='n')
plt.plot(v, m, label='m')
plt.plot(v, h, label='h')
plt.legend(loc='best')
plt.xlabel("vt")
plt.savefig("../results/p1-mnh-small current.jpg")
plt.show()

# proper current
I = np.ones(T) * 10
v, n, m, h = hh.calculate_voltage(v_rest, I, params)

plt.plot(t, v)
plt.savefig("../results/p1-q8 proper current.jpg")
plt.show()
plt.plot(v, n, label='n')
plt.plot(v, m, label='m')
plt.plot(v, h, label='h')
plt.legend(loc='best')
plt.xlabel("vt")
plt.savefig("../results/p1-mnh-proper current.jpg")
plt.show()

# large current
I = np.ones(T) * 200
v, n, m, h = hh.calculate_voltage(v_rest, I, params)

plt.plot(t, v)
plt.savefig("../results/p1-q8 large current.jpg")
plt.show()
plt.plot(v, n, label='n')
plt.plot(v, m, label='m')
plt.plot(v, h, label='h')
plt.legend(loc='best')
plt.xlabel("vt")
plt.savefig("../results/p1-mnh-large current.jpg")
plt.show()

''' Question 9 '''

# sinus current
I = 10 * np.sin(np.arange(0, duration, dt))
v, n, m, h = hh.calculate_voltage(v_rest, I, params)
plt.subplot(2, 1, 1)
plt.plot(t, v, label="Sinus input current")
plt.subplot(2, 1, 2)
plt.plot(t, I, color="red")
plt.savefig("../results/p1-sinus current.jpg")
plt.show()

# pulse current
I = np.zeros(T)
I[1000:3500] = 10
v, n, m, h = hh.calculate_voltage(v_rest, I, params)
plt.subplot(2, 1, 1)
plt.plot(t, v, label="Pulse input current")
plt.subplot(2, 1, 2)
plt.plot(t, I, color="red")
plt.savefig("../results/p1-pulse current.jpg")
plt.show()

# triangle wave
I = sawtooth(2 * np.pi * 0.05 * t) * 10
v, n, m, h = hh.calculate_voltage(v_rest, I, params)
plt.subplot(2, 1, 1)
plt.plot(t, v, label="triangle input current")
plt.subplot(2, 1, 2)
plt.plot(t, I, color="red")
plt.savefig("../results/p1-triangle current.jpg")
plt.show()

# chirp current
I = chirp(t, f0=0.06, f1=0.01, t1=10, method='linear') * 10
v, n, m, h = hh.calculate_voltage(v_rest, I, params)
plt.subplot(2, 1, 1)
plt.plot(t, v, label="chirp input current")
plt.subplot(2, 1, 2)
plt.plot(t, I, color="red")
plt.savefig("../results/p1-chirp current.jpg")
plt.show()

''' 
    Question 10
'''
values=np.arange(0,50,1)
firing_rate=np.zeros(50)
for i in range(50):
    I=values[i]*np.ones(T)
    f=hh.get_firing_rate(v_rest,I,params)
    firing_rate[i]=f
plt.plot(values,firing_rate)
plt.savefig("../results/p1-firing rate-I plot.jpg")
plt.show()