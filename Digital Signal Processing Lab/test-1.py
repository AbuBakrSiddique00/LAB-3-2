
import numpy as np
import matplotlib.pyplot as plt

# Given parameters
fs = 1000          # Sampling frequency (Hz)
fc = 200           # Cutoff frequency (Hz)
N = 21             # Filter length
M = (N - 1) // 2   # Center index

# Step 1: Normalized digital cutoff frequency
wc = 2 * np.pi * fc / fs
# print(f"Cutoff frequency = {wc:.6f} rad/sample")

# Step 2: Ideal impulse response
n = np.arange(N)
print(n)
k = n - M

hd = np.zeros(N)
for i in range(N):
    if k[i] == 0:
        hd[i] = wc / np.pi
    else:
        hd[i] = np.sin(wc * k[i]) / (np.pi * k[i])

# Step 3: Hamming window
w = 0.54 - 0.46 * np.cos(2 * np.pi * n / (N - 1))

# Step 4: Final FIR coefficients
h = hd * w

# print("\nFinal FIR coefficients:")
# for i, value in enumerate(h):
#     print(f"h[{i:2d}] = {value:.8f}")

# print(f"\nSum of coefficients = {np.sum(h):.8f}")

# Step 5: Transfer function frequency response using FFT
nfft = 4096
H = np.fft.rfft(h, n=nfft)
f = np.fft.rfftfreq(nfft, d=1/fs)

magnitude = np.abs(H)
magnitude_db = 20 * np.log10(np.maximum(magnitude, 1e-12))

# Plot 1: Ideal impulse response
plt.figure(figsize=(8, 4))
plt.stem(n, hd)
plt.title("Ideal Impulse Response")
plt.xlabel("Sample index n")
plt.ylabel("Amplitude")
plt.grid(True)
plt.tight_layout()

# Plot 2: Hamming window
plt.figure(figsize=(8, 4))
plt.stem(n, w)
plt.title("Hamming Window (N = 21)")
plt.xlabel("Sample index n")    
plt.ylabel("Amplitude")
plt.grid(True)
plt.tight_layout()

# Plot 3: Final FIR impulse response
plt.figure(figsize=(8, 4))
plt.stem(n, h)
plt.title("Final FIR Filter Coefficients")
plt.xlabel("Sample index n")
plt.ylabel("Amplitude")
plt.grid(True)
plt.tight_layout()

# Plot 4: Frequency response in dB
plt.figure(figsize=(9, 4.5))
plt.plot(f, magnitude_db)
plt.axvline(fc, linestyle="--", label="Cutoff = 200 Hz")
plt.title("FIR Low-Pass Filter Frequency Response Using FFT")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude (dB)")
plt.xlim(0, fs / 2)
plt.ylim(-80, 5)
plt.grid(True)
plt.legend()
plt.tight_layout()

plt.show()
