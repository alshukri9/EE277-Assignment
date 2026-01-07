import numpy as np
import matplotlib.pyplot as plt

n_samples = 10000

n = 30

expected_x = 3.5
expected_y = 3.5*n

y = []

for i in range(n_samples):
    result = 0
    for j in range(n):
        result += np.random.randint(1, 7)

    y.append(result)

print(f"Expected Value of y: {expected_y}")
plt.hist(y, bins=30, density=True)

plt.show()