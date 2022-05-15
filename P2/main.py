import numpy as np
import Izhikevich as izikevich
import matplotlib.pyplot as plt

dt = 0.01
duration = 100
v_rest = -65
u0 = 0

t = int(duration / dt)
T = np.arange(0, t) * dt
t_start = 1000
'''  Tonic Spiking '''
h = 15
params = {
    "dt": dt,
    "duration": duration,
    "a": 0.02,
    "b": 0.2,
    "c": -65,
    "d": 2
}
I = np.zeros(t)
I[t_start:] = h
v, u = izikevich.izhikevich_model(v_rest, I, params)
plt.xlabel("time (ms)")
plt.ylabel("V (mV)")
plt.plot(T, v )
plt.savefig("../results/p2-tonic spiking.jpg")
plt.show()

'''  Phasic Spiking '''
params['a'], params['b'], params['c'], params['d'] = 0.02, 0.25, -65, 6
I[t_start:] = 1
v, u = izikevich.izhikevich_model(v_rest, I, params)
plt.xlabel("time (ms)")
plt.ylabel("V (mV)")
plt.plot(T, v )
plt.savefig("../results/p2-phasic spiking.jpg")
plt.show()

'''  Tonic Bursting '''
params['a'], params['b'], params['c'], params['d'] = 0.02, 0.2, -50, 2
I[t_start:] = 15
v, u = izikevich.izhikevich_model(v_rest, I, params)
plt.xlabel("time (ms)")
plt.ylabel("V (mV)")
plt.plot(T, v )
plt.savefig("../results/p2-tonic bursting.jpg")
plt.show()

'''  Phasic Bursting '''
params['a'], params['b'], params['c'], params['d'] = 0.02, 0.25, -55, 0.05
I[t_start:] = 0.6
v, u = izikevich.izhikevich_model(v_rest, I, params)
plt.xlabel("time (ms)")
plt.ylabel("V (mV)")
plt.plot(T, v )
plt.savefig("../results/p2-phasic bursting.jpg")
plt.show()

'''  Mixed Model '''
params['a'], params['b'], params['c'], params['d'] = 0.02, 0.2, -55, 4
I[t_start:] = 10
v, u = izikevich.izhikevich_model(v_rest, I, params)
plt.xlabel("time (ms)")
plt.ylabel("V (mV)")
plt.plot(T, v )
plt.savefig("../results/p2-mixed model.jpg")
plt.show()

'''  V-U plot for Phasic Spiking '''
params['a'], params['b'], params['c'], params['d'] = 0.02, 0.25, -65, 6
I[t_start:] = 1
v, u = izikevich.izhikevich_model(v_rest, I, params)
plt.xlabel("V (mV)")
plt.ylabel("U (mV)")
plt.plot(v, u)
plt.savefig("../results/p2-V-U phasic spiking.jpg")
plt.show()
