import numpy as np
import matplotlib.pyplot as plt 

amplitude = 1
frequency = 3 / 20
frequency_z = 1 / 60

sampling_rate = 200
duration = 60
t = np.arange(0, duration, 1 / sampling_rate)

y = amplitude * np.sin(2 * np.pi * frequency * t + 0)
z = amplitude * np.sin(2 * np.pi * frequency_z* t +  np.pi)

plt.figure(figsize=(10, 4))
plt.plot(t, y)
plt.plot(t, z)
plt.title("5 Hz Sine Wave")
plt.xlabel("Time (Seconds)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.show()
