
import random as rd
import numpy as np
import math
import time

n = 2
x = [[rd.randint(-10, 10) for x in range(n)] for y in range(n)]
y = [[rd.randint(-10, 10) for x in range(n)] for y in range(n)]
z = np.dot(x, y)
print(np.matrix(x))
print(np.matrix(y))
print(np.matrix(z))

inputs = [1, 2, 3, 2.5]
weights = [[0.2, 0.8, -0.5, 1.0],
           [0.5, -0.91, 0.26, -0.5],
           [-0.26, -0.27, 0.17, 0.87]]
biases = [2, 3, 0.5]

output = np.dot(weights, inputs) + biases
print(output)
