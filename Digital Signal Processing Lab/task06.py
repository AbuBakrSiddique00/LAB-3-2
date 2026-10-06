# No. 6 Task:

import numpy as np
import matplotlib.pyplot as plt

m = np.array([-2, -1, 0, 1, 2, 3])
x = np.array([1, 2, 4, 3, 2, 1])

k = 3

m_right = m + k
m_left = m - k

fig, ax = plt.subplots(3, 1, figsize=(10, 9))

ax[0].stem(m, x)
ax[0].set_title("Original Signal x[m]")
ax[0].set_xlabel("m")
ax[0].set_ylabel("Amplitude")
ax[0].grid(True, alpha=0.3)

ax[1].stem(m_right, x)
ax[1].set_title(f"Right Shift by {k}: x[m-{k}]")
ax[1].set_xlabel("m")
ax[1].set_ylabel("Amplitude")
ax[1].grid(True, alpha=0.3)

ax[2].stem(m_left, x)
ax[2].set_title(f"Left Shift by {k}: x[m+{k}]")
ax[2].set_xlabel("m")
ax[2].set_ylabel("Amplitude")
ax[2].grid(True, alpha=0.3)

plt.tight_layout()
plt.show()