import numpy as np
import matplotlib.pyplot as plt
from scipy import signal


def stem(ax, n, x, title, xlabel="n"):
    ax.stem(n, x)
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.grid(True)

# Z-TRANSFORM & TRANSFER FUNCTION ----------------------------------------
def z_transform_tf():
    # H(z) = (1 + 0.5 z^-1) / (1 - 0.9 z^-1 + 0.81 z^-2)
    b = [1, 0.5]
    a = [1, -0.9, 0.81]
    z = np.roots(b)
    p = np.roots(a)
    print("Zeros:", z)
    print("Poles:", p, "| |p| =", np.abs(p))
    print("Stable (all |p|<1)?", np.all(np.abs(p) < 1))

    w, H = signal.freqz(b, a, 512)
    fig, ax = plt.subplots(1, 3, figsize=(14, 4))
    ax[0].add_patch(plt.Circle((0, 0), 1, fill=False))
    ax[0].plot(z.real, z.imag, "bo", label="zeros")
    ax[0].plot(p.real, p.imag, "rx", label="poles")
    ax[0].set_aspect("equal"); ax[0].legend(); ax[0].grid(True); ax[0].set_title("Pole-zero plot")
    ax[1].plot(w / np.pi, 20 * np.log10(abs(H))); ax[1].set_title("Magnitude (dB)")
    ax[1].set_xlabel("x pi rad/sample"); ax[1].grid(True)
    ax[2].plot(w / np.pi, np.unwrap(np.angle(H))); ax[2].set_title("Phase (rad)")
    ax[2].set_xlabel("x pi rad/sample"); ax[2].grid(True)
    fig.tight_layout()

def main():
    z_transform_tf()
    plt.show()


if __name__ == "__main__":
    main()