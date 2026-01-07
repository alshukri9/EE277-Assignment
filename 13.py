import math
import matplotlib.pyplot as plt
from scipy.stats import poisson as po
import numpy as np

lam = 1

def poisson(lam, upper):
    x = range(upper)
    y = []
    for i in x:
        y.append(po.pmf(i, lam))
    return x, y

def exponential(lam, linspace):
    y = lam*np.exp(-1*lam*linspace)
    return y

x_poisson, y_poisson = poisson(lam, 30)

cdf_poisson = []
holder = 0
for i in range(len(y_poisson)):
    cdf_poisson.append(holder + y_poisson[i])
    holder = holder + y_poisson[i]


x_exp = np.linspace(0, 10, 100)
y_exp = exponential(lam, x_exp)

cdf_exp = []
holder = 0

for val in x_exp:
    cdf_exp.append(1-np.exp(-1*lam*val))

fig, ax = plt.subplots(2,2)

ax[0][0].bar(x_poisson, y_poisson)
ax[0][0].set_title("pdf_poisson")
ax[0][1].plot(x_poisson, cdf_poisson)
ax[0][1].set_title("cdf_poisson")

ax[1][0].plot(x_exp, y_exp)
ax[1][0].set_title("pdf_exp")
ax[1][1].plot(x_exp, cdf_exp)
ax[1][1].set_title("cdf-exp")


plt.show()