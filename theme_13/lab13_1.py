import numpy as np

matrix = np.zeros((3, 4))

np.fill_diagonal(matrix, 5)

matrix[0, 1] = 4
matrix[1, 2] = 4
matrix[2, 3] = 4

print(matrix)
