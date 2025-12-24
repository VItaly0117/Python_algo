import matplotlib.pyplot as plt
import numpy as np
import math

# Параметр лямбда
lam = 2

# Функція для розрахунку ймовірності Пуассона
def poisson_prob(k, lam):
    return (lam**k * math.exp(-lam)) / math.factorial(k)

# Значення k (кількість відвідувачів). Візьмемо від 0 до 8, щоб показати "хвіст" розподілу.
k_values = np.arange(0, 9)

# Розрахунок відповідних ймовірностей
probabilities = [poisson_prob(k, lam) for k in k_values]

# Побудова графіка
plt.figure(figsize=(10, 6))
plt.plot(k_values, probabilities, marker='o', linestyle='-', color='b', label='Пуассон (λ=2)')

# Налаштування осей та заголовка
plt.title('Полігон розподілу числа відвідувачів (Розподіл Пуассона, λ=2)', fontsize=14)
plt.xlabel('Кількість відвідувачів (k)', fontsize=12)
plt.ylabel('Ймовірність P(X=k)', fontsize=12)
plt.xticks(k_values) # Встановлюємо цілочисельні поділки на осі X
plt.grid(True, linestyle='--', alpha=0.7)

# Додамо значення ймовірностей над точками для наочності (округлені до 3 знаків)
for i, prob in enumerate(probabilities):
    plt.text(k_values[i], prob + 0.005, f'{prob:.3f}', ha='center', fontsize=9)

plt.show()