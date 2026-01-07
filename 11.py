import math
import matplotlib.pyplot as plt

n = 7
p = 1/6

# binomial pmf
def fx(n, k, p):
    return math.comb(n, k)*((1 - p)**(n-k))*p**k

y = []

for i in range(n+1):
    y.append(fx(n, i, p))

cdf = []
for i in range(len(y)):
    holder = 0
    for j in range(i):
        holder += y[j]
    cdf.append(holder) 


fig, ax = plt.subplots(2,1)

ax[0].set_title("Probability Distribution")
ax[0].bar(range(n+1), y, alpha=0.7)

ax[1].set_title("Cumulative Distribution")
ax[1].plot(range(n+1), cdf)

plt.show()