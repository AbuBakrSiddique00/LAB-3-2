import numpy as np
import matplotlib.pyplot as plt
from scipy import signal


def stem(ax, n, x, title, xlabel="n"):
    ax.stem(n, x)
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.grid(True)

# SAMPLING, QUANTIZATION, A/D CONVERSION, ALIASING -----------------------
def quantize(x, bits):
    levels = 2 ** bits
    xmin, xmax = x.min(), x.max()
    step = (xmax - xmin) / (levels - 1)
    return np.round((x - xmin) / step) * step + xmin


def sampling_quant_aliasing():
    f = 10                                   # analog frequency (Hz)
    t = np.linspace(0, 1, 5000)              # "continuous" time
    xa = np.sin(2 * np.pi * f * t)

    fig, ax = plt.subplots(3, 1, figsize=(10, 10))

    # (a) proper sampling fs > 2f   and (b) aliasing fs < 2f
    for fs, a in [(100, ax[0]), (12, ax[1])]:
        n = np.arange(0, int(fs * 1))
        xs = np.sin(2 * np.pi * f * n / fs)
        a.plot(t, xa, label=f"analog {f} Hz")
        a.stem(n / fs, xs, linefmt="r-", markerfmt="ro", basefmt=" ",
               label=f"fs={fs} Hz")
        alias = abs(f - fs * round(f / fs))
        tag = "OK (fs>2f)" if fs > 2 * f else f"ALIASING -> appears as {alias} Hz"
        a.set_title(f"Sampling at fs={fs} Hz: {tag}")
        a.legend(); a.grid(True)

    # (c) quantization: 3-bit vs 8-bit, SQNR
    fs = 1000
    tt = np.arange(0, 0.2, 1 / fs)
    x = np.sin(2 * np.pi * 10 * tt)
    ax[2].plot(tt, x, label="original")
    for b in (3, 8):
        xq = quantize(x, b)
        sqnr = 10 * np.log10(np.mean(x ** 2) / np.mean((x - xq) ** 2))
        print(f"{b}-bit quantizer: SQNR = {sqnr:.1f} dB (theory ~ {6.02*b+1.76:.1f})")
        ax[2].step(tt, xq, where="mid", label=f"{b}-bit")
    ax[2].set_title("Quantization (A/D conversion = sample + quantize + encode)")
    ax[2].legend(); ax[2].grid(True)
    fig.tight_layout()



def main():
    sampling_quant_aliasing()
    plt.show()


if __name__ == "__main__":
    main()