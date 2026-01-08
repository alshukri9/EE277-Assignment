import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm, poisson as po, uniform as uni, expon


def uniform(a, b): 
    x = np.linspace(a - 2, b + 2, 100)
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
    x = np.linspace(0, 10, 1000)
    y = expon.pdf(x, scale=(1/lam))
    print(f"""
exponential:
        mean: {1/lam}
        variance: {1/(lam**2)}
""")
    return x, y

def poisson(lam):
    x = range(lam + 10)
    y = po.pmf(x, lam)
    print(f"""
poisson:
        mean: {lam}
        variance: {lam}
""")
    return x, y


if __name__ == "__main__":
    fig, ax = plt.subplots(2, 2, figsize=(10, 12))
    
    ax[0][0].grid(True)
    ax[0][1].grid(True)
    ax[1][0].grid(True)
    ax[1][1].grid(True)

    ax[0][0].spines['left'].set_position('zero')
    ax[0][0].spines['bottom'].set_position('zero')

#   uniform
    a = 2
    b = 4
    ax[0][0].plot(*uniform(a, b), color="blue")
    ax[0][0].axvline((b + a)/2, color="black", linestyle='--')
    ax[0][0].set_title("uniform")

#   gaussian
    gaussian_mean = 5
    ax[0][1].plot(*gaussian(mean=gaussian_mean, sigma=4), color="green")
    ax[0][1].axvline(gaussian_mean, color="black", linestyle='--')
    ax[0][1].set_title("gaussian")

    lam= 10
#   expo
    ax[1][0].plot(*exponential(lam=lam), color="red")
    ax[1][0].axvline(1/lam, color="black", linestyle='--')
    ax[1][0].set_title("exponential")

#   poisson
    input, height = poisson(lam=lam) 
    ax[1][1].bar(input, height, color="skyblue")
    ax[1][1].axvline(lam, color="black", linestyle='--')
    ax[1][1].set_title("poisson")

    plt.show()
    