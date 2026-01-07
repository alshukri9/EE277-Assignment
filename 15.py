import numpy as np
import matplotlib.pyplot as plt


final_positions = []

steps = 100
step_size = 1
n_simulations = 1000

p = 1/2

sim = range(n_simulations)
n = range(steps)

for i in sim:
    current_position = 0
    for j in n:
        direction = np.random.binomial(1, p)

        if direction == 0:
            direction = -1
        
        current_position += direction*step_size
    final_positions.append(current_position)
    

mean = sum(final_positions)/n_simulations
print(f"mean: {mean}")

sd = 0
for pos in final_positions:
    sd += ((pos - mean)**2)
standard_deviation = np.sqrt((sd/n_simulations))

print(f"Standard Deviation: {standard_deviation}")
print(f"Min: {min(final_positions)}")
print(f"Max: {max(final_positions)}")


plt.grid(True)
plt.hist(final_positions, bins=20, density=True, alpha=0.7, color='skyblue', edgecolor='black')

plt.show()