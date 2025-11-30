import numpy as np

# === 1. Завантаження даних з URL ===
print("\n[1] Завантаження даних з URL")
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
names = ('sepallength', 'sepalwidth', 'petallength', 'petalwidth', 'species')
iris = np.genfromtxt(url, delimiter=',', dtype=None, names=names, encoding='utf-8')
print("Перші 5 рядків:\n", iris[:5])

# === 2. Кількість рядків і стовпців ===
print("\n[2] Кількість рядків і стовпців")
print("Рядків:", iris.shape[0])
print("Стовпців:", len(iris.dtype.names))

# === 3. Середнє значення кожного числового параметра ===
print("\n[3] Середнє значення для кожного параметра")
for col in names[:-1]:
    print(f"{col}: {np.mean(iris[col]):.2f}")

# === 4. Мінімум і максимум ===
print("\n[4] Мінімум і максимум по кожному стовпцю")
for col in names[:-1]:
    print(f"{col}: min={np.min(iris[col]):.1f}, max={np.max(iris[col]):.1f}")

# === 5. Медіана ===
print("\n[5] Медіана для кожного стовпця")
for col in names[:-1]:
    print(f"{col}: {np.median(iris[col]):.2f}")

# === 6. Дисперсія і стандартне відхилення ===
print("\n[6] Дисперсія і стандартне відхилення")
for col in names[:-1]:
    print(f"{col}: σ={np.std(iris[col]):.2f}, var={np.var(iris[col]):.2f}")

# === 7. Вибірка тільки для виду 'Iris-setosa' ===
print("\n[7] Вибірка для Iris-setosa")
setosa = iris[iris['species'] == 'Iris-setosa']
print("Кількість рядків Iris-setosa:", len(setosa))

# === 8. Середня довжина чашолистика для кожного виду ===
print("\n[8] Середня довжина чашолистика для кожного виду")
species = np.unique(iris['species'])
for s in species:
    avg = np.mean(iris['sepallength'][iris['species'] == s])
    print(f"{s}: {avg:.2f}")

# === 9. Максимальна ширина пелюстки у Virginica ===
print("\n[9] Максимальна ширина пелюстки у Iris-virginica")
virginica_max = np.max(iris['petalwidth'][iris['species'] == 'Iris-virginica'])
print("Результат:", virginica_max)

# === 10. Мінімальна довжина пелюстки у Versicolor ===
print("\n[10] Мінімальна довжина пелюстки у Iris-versicolor")
versicolor_min = np.min(iris['petallength'][iris['species'] == 'Iris-versicolor'])
print("Результат:", versicolor_min)

# === 11. Сортування за довжиною чашолистика ===
print("\n[11] Сортування за sepallength")
sorted_iris = np.sort(iris, order='sepallength')
print("Перші 3 після сортування:\n", sorted_iris[:3])

# === 12. Нормалізація числових колонок (0–1) ===
print("\n[12] Нормалізація числових даних (0–1)")
for col in names[:-1]:
    norm = (iris[col] - np.min(iris[col])) / (np.max(iris[col]) - np.min(iris[col]))
    print(f"{col} (перші 3): {norm[:3]}")

# === 13. Фільтр: petalwidth > 1.5 ===
print("\n[13] Кількість рядків, де petalwidth > 1.5")
mask = iris['petalwidth'] > 1.5
print("Результат:", np.sum(mask))

# === 14. Середнє співвідношення petalwidth/petallength ===
print("\n[14] Середнє співвідношення petalwidth/petallength")
ratio = iris['petalwidth'] / iris['petallength']
print("Результат:", np.mean(ratio))

# === 15. Булевий масив sepallength > 5 ===
print("\n[15] Булевий масив sepallength > 5")
mask2 = iris['sepallength'] > 5
print(mask2[:10])

# === 16. Унікальні значення виду ===
print("\n[16] Унікальні значення виду")
print(np.unique(iris['species']))

# === 17. Підрахунок кількості квітів кожного виду ===
print("\n[17] Кількість квітів кожного виду")
for s in species:
    print(f"{s}: {np.sum(iris['species'] == s)} шт.")

# === 18. Перевірка співвідношення середніх параметрів ===
print("\n[18] Співвідношення середніх значень sepallength/sepalwidth")
ratio_mean = np.mean(iris['sepallength']) / np.mean(iris['sepalwidth'])
print("Результат:", round(ratio_mean, 3))
