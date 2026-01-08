import matplotlib.pyplot as plt
from scipy.stats import poisson, expon
import numpy as np

lam = 30

fig, ax = plt.subplots(2,2)

x_poisson = range(lam + 10)

ax[0][0].bar(x_poisson, poisson.pmf(x_poisson, lam))
ax[0][0].set_title("pdf_poisson")
ax[0][1].bar(x_poisson, poisson.cdf(x_poisson, lam))
ax[0][1].set_title("cdf_poisson")

x_expon = np.linspace(0, 10, 100)

ax[1][0].grid(True)
ax[1][1].grid(True)

ax[1][0].plot(x_expon, expon.pdf(x_expon, scale=1/lam))
ax[1][0].set_title("pdf_exp")
ax[1][1].plot(x_expon, expon.cdf(x_expon, scale=1/lam))
ax[1][1].set_title("cdf-exp")


plt.show()