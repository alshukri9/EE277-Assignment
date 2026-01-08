import numpy as np
import matplotlib.pyplot as plt


steps = 10
step_size = 1
simulations = 1000
p = 1/2

def random_walk(p, n_steps, step_size, n_simulations):
    final_positions = []
    simulations = range(n_simulations)
    steps = range(n_steps)
    for i in simulations:
        current_position = 0
        for _ in steps:
            direction = np.random.binomial(1, p)

            if direction == 0:
                direction = -1
            
            current_position += direction*step_size
        final_positions.append(current_position)
    
    return final_positions
    
final_positions = random_walk(p, steps, step_size, simulations)
mean = sum(final_positions)/simulations
print(f"mean: {mean}")

sd = 0
for pos in final_positions:
    sd += ((pos - mean)**2)
standard_deviation = np.sqrt((sd/simulations))

print(f"Standard Deviation: {standard_deviation}")
print(f"Min: {min(final_positions)}")
print(f"Max: {max(final_positions)}")

plt.grid(True)
plt.hist(final_positions, bins=20, density=True, alpha=0.7, color='skyblue', edgecolor='black')

plt.show()