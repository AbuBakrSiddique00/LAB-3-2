import numpy as np
import matplotlib.pyplot as plt
from scipy import signal


def stem(ax, n, x, title, xlabel="n"):
    ax.stem(n, x)
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.grid(True)


# CORRELATION -------------------------------------------------------------
def correlation():
    rng = np.random.default_rng(0)
    x = rng.standard_normal(200)
    delay = 15
    y = np.concatenate([np.zeros(delay), x])[:200] + 0.2 * rng.standard_normal(200)

    rxy = signal.correlate(y, x, mode="full")
    lags = signal.correlation_lags(len(y), len(x), mode="full")
    rxx = signal.correlate(x, x, mode="full")

    print("Estimated delay from cross-correlation peak:", lags[np.argmax(rxy)])
    fig, ax = plt.subplots(2, 1, figsize=(9, 6))
    ax[0].plot(lags, rxx); ax[0].set_title("Autocorrelation of x (peak at lag 0)"); ax[0].grid(True)
    ax[1].plot(lags, rxy); ax[1].set_title(f"Cross-correlation x,y (peak at lag {delay})"); ax[1].grid(True)
    fig.tight_layout()

def main():
    correlation()
    plt.show()


if __name__ == "__main__":
    main()