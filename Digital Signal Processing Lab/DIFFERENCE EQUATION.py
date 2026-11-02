import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

def stem(ax, n, x, title, xlabel="n"):
    ax.stem(n, x)
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.grid(True)

# DIFFERENCE EQUATION -----------------------------------------------------
def difference_equation():
    # y(n) - 0.5 y(n-1) = x(n)   ->  b=[1], a=[1,-0.5]
    b, a = [1], [1, -0.5]
    n = np.arange(0, 20)
    imp = (n == 0).astype(float)
    stp = np.ones_like(n, dtype=float)
    h = signal.lfilter(b, a, imp)      # impulse response (theory: 0.5^n)
    s = signal.lfilter(b, a, stp)      # step response

    # manual recursion to verify
    y = np.zeros(len(n))
    for k in range(len(n)):
        y[k] = imp[k] + (0.5 * y[k - 1] if k > 0 else 0)
    print("Manual recursion == lfilter:", np.allclose(y, h))

    fig, ax = plt.subplots(2, 1, figsize=(8, 6))
    stem(ax[0], n, h, "Impulse response h(n) = 0.5^n u(n)")
    stem(ax[1], n, s, "Step response")
    fig.tight_layout()


def main():
    difference_equation()
    plt.show()


if __name__ == "__main__":
    main()