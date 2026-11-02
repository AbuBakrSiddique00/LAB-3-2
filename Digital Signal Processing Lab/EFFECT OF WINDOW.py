import numpy as np
import matplotlib.pyplot as plt
from scipy import signal


def stem(ax, n, x, title, xlabel="n"):
    ax.stem(n, x)
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.grid(True)

# EFFECT OF WINDOW -------------------------------------------------------
def window_effect():
    N = 64
    n = np.arange(N)
    x = np.sin(2 * np.pi * 10.5 * n / N)       # non-integer bin -> leakage
    NF = 1024

    fig, ax = plt.subplots(2, 1, figsize=(10, 8))
    for name in ["boxcar", "hann", "hamming", "blackman"]:
        w = signal.get_window(name, N)
        X = np.abs(np.fft.fft(x * w, NF))[: NF // 2]
        ax[0].plot(20 * np.log10(X / X.max() + 1e-12), label=name)
    ax[0].set_ylim(-100, 5); ax[0].legend(); ax[0].grid(True)
    ax[0].set_title("Spectral leakage with different windows (rect = worst sidelobes)")

    for name in ["boxcar", "hamming", "blackman"]:
        h = signal.firwin(51, 0.3, window=name)
        w, H = signal.freqz(h, 1, 1024)
        ax[1].plot(w / np.pi, 20 * np.log10(abs(H) + 1e-12), label=name)
    ax[1].set_ylim(-120, 5); ax[1].legend(); ax[1].grid(True)
    ax[1].set_title("FIR low-pass design: window trade-off (narrow main lobe vs low sidelobes)")
    fig.tight_layout()


def main():
    window_effect()
    plt.show()


if __name__ == "__main__":
    main()