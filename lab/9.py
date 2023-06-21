import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5, 5, 1000)
y = np.log(np.abs((x ** 2) - 1) + 0.5)
x += np.random.normal(scale=0.2, size=1000)
plt.scatter(x, y, alpha=0.3)


def lr(x0, x, y, tau):
    x0 = np.r_[1, x0]
    x = np.c_[np.ones(len(x)), x]
    xw = x.T * radial(x0, x, tau)
    beta = np.linalg.pinv(xw @ x) @ xw @ y
    return beta @ x0


def radial(x0, x, tau):
    return np.exp(np.sum((x - x0) ** 2, axis=1) / (-2 * tau ** 2))


def plots(tau):
    domain = x
    pred = [lr(x0, x, y, tau) for x0 in domain]
    plt.scatter(x, y, alpha=0.3)
    plt.plot(domain, pred, color="red")
    return plt


plots(1).show()
