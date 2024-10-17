import numpy as np

data = np.genfromtxt('example_numpy.csv', delimiter=',', skip_header=1)
mean_values = np.mean(data, axis=0)

print(mean_values)
