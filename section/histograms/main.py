import matplotlib.pyplot as plt
import numpy as np

size = 1000
normal_sample = np.random.normal(size=size)

# Create a probabilty density function approximation using a histogram
n = len(normal_sample)
plt.hist(normal_sample, bins = 1 + int(np.log2(n)), density=True)

plt.show()