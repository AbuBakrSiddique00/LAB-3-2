import numpy as np
import matplotlib.pyplot as plt

# Input two sequences
x = np.array([1, 2, 3])
h = np.array([1, 2])

# Find convolution
y = np.convolve(x, h)

print("First sequence:", x)
print("Second sequence:", h)
print("Convolution of two sequences:", y)   

# Plot
plt.stem(y)
plt.xlabel("n")
plt.ylabel("Amplitude")
plt.title("Convolution of Two Sequences")
plt.grid(True)
plt.show()