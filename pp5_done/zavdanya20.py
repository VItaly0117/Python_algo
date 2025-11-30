import numpy as np
# --- 1. Створіть одновимірний масив чисел від 0 до 9 ---
print("--- 1 ---")
arr1 = np.arange(10)
print(arr1)

# --- 2. Створіть масив розміром 3 × 3 зі значеннями True ---
print("\n--- 2 ---")
arr2 = np.full((3, 3), True, dtype=bool)
# Альтернативний варіант:
# arr2 = np.ones((3, 3), dtype=bool)
print(arr2)

# --- 3. Залиште в масиві лише непарні числа (a%2 == 1) ---
print("\n--- 3 ---")
a = np.arange(10)
arr3 = a[a % 2 == 1]
print(arr3)

# --- 4. Замініть в масиві усі непарні числа на -1 ---
print("\n--- 4 ---")
arr4 = np.arange(10)
arr4[arr4 % 2 == 1] = -1
print(arr4)

# --- 5. Утворіть новий масив, замінивши непарні числа на -1 ---
print("\n--- 5 ---")
a = np.arange(10)
arr5 = np.where(a % 2 == 1, -1, a)
print(f"Оригінальний масив 'a': {a}")
print(f"Новий масив 'arr5':     {arr5}")

# --- 6. Перетворіть 1D-масив на 2D-масив із 2 рядками ---
print("\n--- 6 ---")
arr6 = np.arange(10).reshape(2, -1) # -1 автоматично розрахує кількість стовпців
print(arr6)

# --- 7. Складіть масиви a і b вертикально ---
print("\n--- 7 ---")
a = np.arange(1, 6)
b = np.arange(6, 11)
arr7 = np.vstack([a, b])
# Альтернативний варіант:
# arr7 = np.concatenate([a.reshape(1, -1), b.reshape(1, -1)], axis=0)
print(arr7)

# --- 8. Складіть масиви a і b горизонтально ---
print("\n--- 8 ---")
a = np.arange(1, 6)
b = np.arange(6, 11)
arr8 = np.hstack([a, b])
# Альтернативний варіант:
# arr8 = np.concatenate([a, b], axis=0)
print(arr8)

# --- 9. Отримайте спільні елементи масивів a і b ---
print("\n--- 9 ---")
a = np.array([1, 2, 3, 4, 5])
b = np.array([4, 5, 6, 7, 8])
arr9 = np.intersect1d(a, b)
print(arr9)

# --- 10. З масиву a видалити всі елементи, присутні в масиві b ---
print("\n--- 10 ---")
a = np.array([1, 2, 3, 4, 5])
b = np.array([4, 5, 6, 7, 8])
arr10 = np.setdiff1d(a, b)
print(arr10)

# --- 11. Визначити позиції, на яких елементи масивів a і b співпадають ---
print("\n--- 11 ---")
a = np.array([1, 2, 3, 4, 5])
b = np.array([1, 9, 3, 4, 9])
arr11 = np.where(a == b)
print(arr11) # Повертає кортеж індексів

# --- 12. Елементи від 5 до 10 із заданого масиву ---
print("\n--- 12 ---")
a = np.arange(15)
arr12 = a[(a >= 5) & (a <= 10)]
print(arr12)

# --- 13. Перетворіть функцію maxx на роботу з двома масивами ---
print("\n--- 13 ---")
def maxx(x, y):
    if x >= y:
        return x
    else:
        return y

# Векторизуємо функцію
vectorized_maxx = np.vectorize(maxx)

a = np.array([1, 5, 10])
b = np.array([2, 3, 9])
arr13 = vectorized_maxx(a, b)
print(arr13)
# Примітка: для простого максимуму краще використовувати np.maximum(a, b)

# --- 14. Поміняйте в масиві місцями стовпці 1 і 2 ---
print("\n--- 14 ---")
arr = np.arange(9).reshape(3, 3)
print("Оригінал:")
print(arr)
# [:, [0, 2, 1]] - це просунуте індексування
arr14 = arr[:, [0, 2, 1]]
print("Результат:")
print(arr14)

# --- 15. Поміняйте в масиві місцями рядки 2 і 3 ---
print("\n--- 15 ---")
arr = np.arange(12).reshape(4, 3)
print("Оригінал:")
print(arr)
# Індекси: 0, 1, 3, 2
arr15 = arr[[0, 1, 3, 2], :]
print("Результат:")
print(arr15)

# --- 16. Поміняйте порядок рядків на зворотний ---
print("\n--- 16 ---")
arr = np.arange(9).reshape(3, 3)
print("Оригінал:")
print(arr)
arr16 = arr[::-1, :]
# Альтернатива: arr16 = np.flip(arr, axis=0)
print("Результат:")
print(arr16)

# --- 17. Поміняйте порядок стовпців на зворотний ---
print("\n--- 17 ---")
arr = np.arange(9).reshape(3, 3)
print("Оригінал:")
print(arr)
arr17 = arr[:, ::-1]
# Альтернатива: arr17 = np.flip(arr, axis=1)
print("Результат:")
print(arr17)

# --- 18. Створіть 2D-масив 5x3 (випадкові числа від 5 до 10) ---
print("\n--- 18 ---")
# np.random.rand(5, 3) дає числа від 0 до 1
# (10 - 5) * ... + 5 -> масштабує до діапазону [5, 10)
arr18 = (10 - 5) * np.random.rand(5, 3) + 5
print(arr18)

# --- 19. Округлення до 3-го знаку ---
print("\n--- 19 ---")
arr = np.random.rand(3, 3)
print("Оригінал:")
print(arr)
# Використання np.set_printoptions
np.set_printoptions(precision=3)
print("Результат (округлено):")
print(arr)
# Скидання налаштувань (за бажанням)
np.set_printoptions(precision=8)

# --- 20. Виведення без експоненційного формату ---
print("\n--- 20 ---")
arr20 = np.array(
    [[5.434049e-02, 2.783694e-02, 4.245176e-03],
     [8.447761e-02, 4.718856e-03, 1.215691e-02],
     [6.707491e-02, 8.258528e-02, 1.367066e-01]])

np.set_printoptions(suppress=True, precision=8) # suppress=True вимикає експоненту
print(arr20)
np.set_printoptions(suppress=False) # Повертаємо назад

# --- 21. Обмеження кількості елементів при виведенні ---
print("\n--- 21 ---")
arr_large = np.arange(100)
print("Оригінальний вивід (скорочений за замовчуванням):")
print(arr_large)

# Обмежуємо до 6 елементів
np.set_printoptions(threshold=6)
print("\nВивід, обмежений до 6 елементів:")
print(arr_large)

# Як вивести всі елементи
import sys
np.set_printoptions(threshold=sys.maxsize)
print("\nВивід усіх 100 елементів (примусово):")
print(arr_large)

# Повертаємо до стандартного
np.set_printoptions(threshold=1000)

# --- 22. Вставте 5 значень np.nan у випадкових позиціях ---
print("\n--- 22 ---")
arr22 = np.arange(9).reshape(3, 3).astype(float) # Робимо float для nan
rand_indices_rows = np.random.randint(0, 3, size=5)
rand_indices_cols = np.random.randint(0, 3, size=5)

arr22[rand_indices_rows, rand_indices_cols] = np.nan
print(arr22)

# --- 23. Замініть усі nan на 0 ---
print("\n--- 23 ---")
# Використовуємо масив з попереднього кроку
arr22[np.isnan(arr22)] = 0
arr23 = arr22
print(arr23)

# --- 24. Замініть значення > 30 на 30, а < 10 на 10 ---
print("\n--- 24 ---")
arr24 = np.random.randint(0, 50, size=(5, 5))
print("Оригінал:")
print(arr24)

arr24_clipped = np.clip(arr24, a_min=10, a_max=30)
# Альтернатива:
# arr24[arr24 < 10] = 10
# arr24[arr24 > 30] = 30
print("Результат (обмежено 10-30):")
print(arr24_clipped)