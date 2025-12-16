import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-np.sqrt(3), np.sqrt(3),500)
y = np.cbrt(x**2) + np.sqrt(3 - x**2) * np.sin(16 * np.pi * x)

data = np.column_stack((x, y))
plt.plot(x, y,'red')
plt.ylim(-3, 3)
plt.xlim(-3, 3)
plt.grid(True)
plt.show()

#np.savetxt("data.txt", data, fmt="%.6f", delimiter="\t")
