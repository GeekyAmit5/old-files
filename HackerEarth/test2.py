import numpy as np


def f(p):
    return np.array([[7, -4, 4], [4, 2, 8], [p, -8, 28]])


sol = [29, 16, 14, 21]
for i in sol:
    if np.linalg.det(f(i)) < 10**(-10):
        print(i)
