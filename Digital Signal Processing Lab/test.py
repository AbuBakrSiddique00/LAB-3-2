import numpy as np
import matplotlib.pyplot as plt

# ---------------------------------------------------------
# 1. Functional Representation Definition
# ---------------------------------------------------------
# x(n) = 2*n for 0 <= n <= 4, else 0
def x_functional(n):
    return np.where((n >= 0) & (n <= 4), 2 * n, 0)

n = np.arange(-2, 7)
x_func = x_functional(n)


# ---------------------------------------------------------
# 2. Tabular Representation (Data Pairs)
# ---------------------------------------------------------
# Table Data: n and corresponding x(n)
n_table = np.array([-1,  0,  1,  2,  3,  4,  5])
x_table = np.array([ 0,  1,  3,  5,  2,  0,  0])


# ---------------------------------------------------------
# Plotting both conversions
# ---------------------------------------------------------
plt.figure(figsize=(12, 5))

# Plot 1: Functional to Graphical
plt.subplot(1, 2, 1)
plt.stem(n, x_func)
plt.title("Functional -> Graphical Representation\n$x(n) = 2n$ for $0 \leq n \leq 4$")
plt.xlabel("Time Index (n)")
plt.ylabel("Amplitude x(n)")
plt.grid(True)

# Plot 2: Tabular to Graphical
plt.subplot(1, 2, 2)
plt.stem(n_table, x_table)
plt.title("Tabular -> Graphical Representation\n(Plotted from Table Data)")
plt.xlabel("Time Index (n)")
plt.ylabel("Amplitude x(n)")
plt.grid(True)

plt.tight_layout()
plt.show()