import numpy as np
n = int(input("n: "))
r = float(input("r: "))
dobfactorial_array = np.arange(n, 0, -2)
dobfactorial = np.prod(dobfactorial_array)
power = np.power(2 * r, n)
exponent = n // 2
pi_power = np.power(np.pi / 2, exponent)
result = (power * pi_power) / dobfactorial
print("Результат:", result)