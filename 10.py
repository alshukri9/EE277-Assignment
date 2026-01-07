import numpy as np


x = np.random.randint(-10, 10, 20)

print(x)

def mean(data):
    return sum(data)/len(data)

def variance(data):
    m = mean(data)
    y = 0
    for value in data:
        y += (value - m)**2
    return y/len(data)    


print(f"mean: {mean(x)} variance: {variance(x)}")