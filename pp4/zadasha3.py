import numpy as np
n = int(input("n: "))
a = np.array([float(input(f"a[{i}]: ")) for i in range(1, n + 1)])
multipliers = np.arange(1, n + 1)
min_value = (a * multipliers).min()
print("Minimalni dobytok:", min_value)