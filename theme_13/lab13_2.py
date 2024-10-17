import numpy as np

matrix = np.array([[5, 4, 0, 0],
                   [0, 5, 4, 0],
                   [0, 0, 5, 4]])

vertical_vector = matrix.reshape(-1, 1) 

print(vertical_vector)
