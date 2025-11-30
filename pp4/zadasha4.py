import numpy as np
vec1 = [1, 2, 3, 4, 5, 5, 6, 7, 8, 9, 10]
vec2 = [3, 4, 2, 4, 9, 7, 8, 5, 5, 6, 7]
# Перетворюємо списки на масиви NumPy
vec1_np = np.array(vec1)
vec2_np = np.array(vec2)
# Знаходимо перетин (спільні елементи) однією командою
result = np.intersect1d(vec1_np, vec2_np)
print("Spilni elementi:", result)