import numpy as np
import matplotlib.pyplot as plt

def simulate_markov_chain(P, initial_dist, steps):
    # P: Transition Matrix
    # initial_dist: Starting probability distribution (e.g., [1, 0, 0])
    # steps: Number of time steps to simulate
    
    n_states = len(initial_dist)
    history = np.zeros((steps + 1, n_states))
    history[0] = initial_dist
    
    current_dist = initial_dist
    for i in range(1, steps + 1):
        # The distribution at step n is: dist(n-1) * P
        current_dist = np.dot(current_dist, P)
        history[i] = current_dist
        
    return history

# Define Transition Matrix (Rows must sum to 1)
# 0: Sunny, 1: Cloudy, 2: Rainy
P = np.array([
    [0.7, 0.2, 0.1],  # From Sunny
    [0.3, 0.4, 0.3],  # From Cloudy
    [0.2, 0.3, 0.5]   # From Rainy
])

# Start with a 100% chance of being Sunny
initial_state = np.array([1.0, 0.0, 0.0])
steps = 15

dist_history = simulate_markov_chain(P, initial_state, steps)

# Plotting the evolution
plt.figure(figsize=(10, 6))
plt.plot(dist_history[:, 0], label='Sunny', marker='o')
plt.plot(dist_history[:, 1], label='Cloudy', marker='s')
plt.plot(dist_history[:, 2], label='Rainy', marker='^')
plt.title("Evolution of State Probabilities Over Time")
plt.xlabel("Step (Time)")
plt.ylabel("Probability")
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()

# Calculate Steady State analytically (Eigenvector approach)
# Solve pi * P = pi
eigenvalues, eigenvectors = np.linalg.eig(P.T)
steady_state = eigenvectors[:, np.isclose(eigenvalues, 1)].real
steady_state = steady_state / steady_state.sum()
print(f"Steady State Probabilities: {steady_state.flatten()}")