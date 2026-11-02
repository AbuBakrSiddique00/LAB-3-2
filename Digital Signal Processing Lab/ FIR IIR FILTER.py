import numpy as np
import matplotlib.pyplot as plt
from scipy import signal


def stem(ax, n, x, title, xlabel="n"):
    ax.stem(n, x)
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.grid(True)


# FIR / IIR FILTER --------------------------------------------------------
def fir_iir():
    fs = 1000
    fc = 100
    t = np.arange(0, 0.5, 1 / fs)
    x = np.sin(2 * np.pi * 50 * t) + 0.7 * np.sin(2 * np.pi * 300 * t)

    h_fir = signal.firwin(51, fc, fs=fs, window="hamming")        # FIR low-pass
    b_iir, a_iir = signal.butter(4, fc, fs=fs)                     # IIR Butterworth

    y_fir = signal.lfilter(h_fir, 1, x)
    y_iir = signal.lfilter(b_iir, a_iir, x)

    w, Hf = signal.freqz(h_fir, 1, 1024, fs=fs)
    _, Hi = signal.freqz(b_iir, a_iir, 1024, fs=fs)

    fig, ax = plt.subplots(2, 1, figsize=(10, 8))
    ax[0].plot(w, 20 * np.log10(abs(Hf) + 1e-12), label="FIR (51 taps, Hamming)")
    ax[0].plot(w, 20 * np.log10(abs(Hi) + 1e-12), label="IIR (Butterworth, order 4)")
    ax[0].set_ylim(-100, 5); ax[0].legend(); ax[0].grid(True)
    ax[0].set_title("Frequency responses"); ax[0].set_xlabel("Hz")
    ax[1].plot(t, x, alpha=0.4, label="input")
    ax[1].plot(t, y_fir, label="FIR out")
    ax[1].plot(t, y_iir, label="IIR out")
    ax[1].legend(); ax[1].grid(True); ax[1].set_title("Filtering (300 Hz removed)")
    fig.tight_layout()



def main():
    fir_iir()
    plt.show()


if __name__ == "__main__":
    main()