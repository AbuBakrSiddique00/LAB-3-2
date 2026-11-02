import numpy as np
import matplotlib.pyplot as plt
from scipy import signal


def stem(ax, n, x, title, xlabel="n"):
    ax.stem(n, x)
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.grid(True)

# CONVOLUTION -------------------------------------------------------------
def conv_manual(x, h):
    y = np.zeros(len(x) + len(h) - 1)
    for i in range(len(x)):
        for j in range(len(h)):
            y[i + j] += x[i] * h[j]
    return y


def convolution():
    x = np.array([1, 2, 3, 4])
    h = np.array([1, 1, 1])
    y1 = conv_manual(x, h)
    y2 = np.convolve(x, h)
    print("Convolution manual :", y1)
    print("Convolution numpy  :", y2, "| match:", np.allclose(y1, y2))
    fig, ax = plt.subplots(3, 1, figsize=(8, 8))
    stem(ax[0], np.arange(len(x)), x, "x(n)")
    stem(ax[1], np.arange(len(h)), h, "h(n)")
    stem(ax[2], np.arange(len(y1)), y1, "y(n) = x(n) * h(n)")
    fig.tight_layout()

def main():
    convolution()
    plt.show()


if __name__ == "__main__":
    main()