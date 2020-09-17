import numpy as np
n = int(input())
print('YES')
x = 2*np.pi/n
for i in range(n):
    print(np.cos(x*i), np.sin(x*i))
