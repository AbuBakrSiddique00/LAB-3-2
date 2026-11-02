import numpy as np
import matplotlib.pyplot as plt
from scipy import signal


def stem(ax, n, x, title, xlabel="n"):
    ax.stem(n, x)
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.grid(True)

# SIGNAL TRANSFORMATION (shift, fold, scale) -----------------------------
def signal_transformation():
    n = np.arange(-6, 7)
    x = np.where((n >= -2) & (n <= 3), n + 3, 0).astype(float)  # sample signal

    def at(sig, idx):          # evaluate sig at (possibly non-integer) indices
        out = np.zeros(len(idx))
        for k, i in enumerate(idx):
            if i == int(i) and n[0] <= i <= n[-1]:
                out[k] = sig[int(i) - n[0]]
        return out

    fig, ax = plt.subplots(2, 3, figsize=(12, 6))
    stem(ax[0, 0], n, x, "x(n)")
    stem(ax[0, 1], n, at(x, n - 2), "x(n-2)  delay by 2")
    stem(ax[0, 2], n, at(x, n + 2), "x(n+2)  advance by 2")
    stem(ax[1, 0], n, at(x, -n), "x(-n)  folding")
    stem(ax[1, 1], n, at(x, 2 * n), "x(2n)  downsample")
    stem(ax[1, 2], n, at(x, n / 2), "x(n/2) upsample (zeros inserted)")
    fig.suptitle("3. Signal transformation"); fig.tight_layout()

def main():
    signal_transformation()  
    plt.show()


if __name__ == "__main__":
    main()