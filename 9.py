import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm, poisson as po, uniform as uni


def uniform(a, b): 
    x = np.linspace(a - 2, b + 2, 1000)
    data = uni.pdf(x, loc=a, scale=(b-a))
    print(f"""
uniform:
        mean: {(b + a)/2}
        variance: {((b - a)**2)/12}
""")
    return x, data

def gaussian(mean, sigma):
    x = np.linspace(mean - 4*sigma, mean + 4*sigma, 1000)
    y = norm.pdf(x, mean, scale=sigma)
    print(f"""
gaussian:
        mean: {mean}
        variance: {sigma**2}
""")
    return x, y

def exponential(lam):
    x = np.linspace(0, 20, 101)
    y = lam*np.exp(-1*lam*x)
    print(f"""
exponential:
        mean: {1/lam}
        variance: {1/(lam**2)}
""")
    return x, y

def poisson(lam, upper):
    x = []
    y = []
    for i in range(upper):
        x.append(i)
        y.append(po.pmf(i, lam))
    print(f"""
poisson:
        mean: {lam}
        variance: {lam}
""")
    return x, y


if __name__ == "__main__":
    fig, ax = plt.subplots(2, 2, figsize=(10, 12))

    ax[0][0].spines['left'].set_position('zero')
    ax[0][0].spines['bottom'].set_position('zero')

    ax[0][0].plot(*uniform(2, 4), color="blue")
    ax[0][0].set_title("uniform")
    ax[0][1].plot(*gaussian(mean=5, sigma=4), color="green")
    ax[0][1].set_title("gaussian")

    ax[1][0].plot(*exponential(lam=0.5), color="red")
    ax[1][0].set_title("exponential")
    ax[1][1].plot(*poisson(lam=10, upper=20))
    ax[1][1].set_title("poisson")

    plt.show()
    