import numpy as np
import matplotlib.pyplot as plt
from scipy import signal


def stem(ax, n, x, title, xlabel="n"):
    ax.stem(n, x)
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.grid(True)


# BASIC SIGNAL GENERATION ------------------------------------------------
def basic_signals():
    n = np.arange(-10, 21)
    impulse = (n == 0).astype(float)
    step = (n >= 0).astype(float)
    ramp = n * step
    expo = (0.8 ** n) * step
    sine = np.sin(2 * np.pi * 0.05 * n)

    t = np.linspace(0, 1, 1000)
    square = signal.square(2 * np.pi * 5 * t)
    saw = signal.sawtooth(2 * np.pi * 5 * t)

    fig, ax = plt.subplots(3, 3, figsize=(12, 8))
    stem(ax[0, 0], n, impulse, "Unit impulse")
    stem(ax[0, 1], n, step, "Unit step")
    stem(ax[0, 2], n, ramp, "Unit ramp")
    stem(ax[1, 0], n, expo, "Exponential 0.8^n u(n)")
    stem(ax[1, 1], n, sine, "Sine (f=0.05)")
    ax[1, 2].plot(t, square); ax[1, 2].set_title("Square wave"); ax[1, 2].grid(True)
    ax[2, 0].plot(t, saw); ax[2, 0].set_title("Sawtooth"); ax[2, 0].grid(True)
    ax[2, 1].axis("off"); ax[2, 2].axis("off")
    fig.suptitle("1. Basic signal generation"); fig.tight_layout()



def main():
    basic_signals()
    plt.show()

if __name__ == "__main__":
    main()