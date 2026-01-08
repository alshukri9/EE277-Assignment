import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
import math


n_samples = 35

p = 0.2
expected_x = p
variance_x = p*(1 - p)

expected_y = n_samples * p
variance_y = n_samples * variance_x

n = range(0, n_samples)

def fx(n, k, p):
    return math.comb(n, k)*((1 - p)**(n-k))*p**k

y = []
for i in n:
    y.append(fx(n_samples, i, p))

print(f"Mean: {expected_y:.2f}")
print(f"Variance {variance_y:.2f}")

plt.bar(n, y, color="skyblue")

plt.show()