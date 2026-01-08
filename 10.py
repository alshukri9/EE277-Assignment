import numpy as np


x = np.random.randint(0, 10, 6)

print(x)

def mean(data):
    return sum(data)/len(data)

def variance(data):
    m = mean(data)
    y = 0
    for value in data:
        y += (value - m)**2
    return y/len(data)    


print(f"mean: {mean(x):.2f} variance: {variance(x):.2f}")