import numpy as np
import matplotlib.pyplot as plt

n = np.linspace(-10, 10)
plt.plot(n, np.sin(n), label="sin(n)")
plt.plot(n, n*0)
plt.show()
