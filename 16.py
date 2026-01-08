import numpy as np
import matplotlib.pyplot as plt

n_samples = 1000
x = np.random.normal(50, 10, n_samples)
y = -0.2 * x + 10

cov_matrix = np.cov(x, y)

covariance_xy = cov_matrix[0,1]
variance_x = cov_matrix[0,0]
variance_y = cov_matrix[1,1]

cc = covariance_xy/np.sqrt(variance_x*variance_y)

print(f"Covariance: {covariance_xy}")
print(f"Correlation Coefficient: {cc}")

plt.scatter(x=x, y=y, alpha=0.5, color='royalblue', edgecolors='w', linewidth=0.5)

plt.xlabel("RV X")
plt.ylabel("RV Y")
plt.grid(True, alpha=0.5)

plt.show()
