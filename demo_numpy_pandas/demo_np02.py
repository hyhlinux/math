import numpy as np

A = np.array([[0, 1, 2], [-3, 4, 0], [-1, 3, -2]])
B = np.array([[-4, -1, 2], [-1, -4, 0], [1, 5, -2]])
print(A, A.shape, B, B.shape)

X = (A+B)/4
# X = A.__add__(B).__div__(4)
Y = B - X
print(X, Y)