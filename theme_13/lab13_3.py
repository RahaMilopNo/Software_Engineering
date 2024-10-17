import numpy as np

x_shape = tuple(map(int, input().split()))
X = np.fromiter(map(int, input().split()), int).reshape(x_shape)

y_shape = tuple(map(int, input().split()))
Y = np.fromiter(map(int, input().split()), int).reshape(y_shape)

if x_shape[1] != y_shape[0]:
    print("формы матриц не совпадают")
else:
    result = np.dot(X, Y)
    print(result)
