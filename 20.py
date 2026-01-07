import numpy as np
import matplotlib.pyplot as plt

n = 10000

def calculate_pi(num_samples):
    x = np.random.uniform(-1, 1, num_samples)
    y = np.random.uniform(-1, 1, num_samples)
    
    distance = np.sqrt(x**2 + y**2)
    
    inside_circle = distance <= 1
    
    pi_estimate = (np.sum(inside_circle) / num_samples)
    
    return pi_estimate, x, y, inside_circle

pi_est, x_vals, y_vals, inside = calculate_pi(n)

samples_range = np.arange(1, n + 1)
cumulative_inside = np.cumsum(inside)
convergence = (cumulative_inside / samples_range) * 4

print(f"Estimated Pi ({n} samples): {pi_est}")
print(f"Exact Value: {np.pi}")
print(f"Error %: {abs(np.pi - pi_est)/np.pi}")

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

ax1.scatter(x_vals[inside], y_vals[inside], color='blue', s=1, label='Inside')
ax1.scatter(x_vals[~inside], y_vals[~inside], color='red', s=1, label='Outside')
ax1.set_title("Monte Carlo Points")
ax1.set_aspect('equal')

ax2.plot(samples_range, convergence, label='Estimated Pi')
ax2.axhline(y=np.pi, color='black', linestyle='--', label='True Pi')
ax2.set_xscale('log')
ax2.set_title("Convergence of Pi")
ax2.set_xlabel("Number of Samples (Log Scale)")
ax2.legend()

plt.show()