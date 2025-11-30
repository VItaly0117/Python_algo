import numpy as np
import matplotlib.pyplot as plt

# === 1. Завантаження даних з URL (з вашого коду) ===
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
names = ('sepallength', 'sepalwidth', 'petallength', 'petalwidth', 'species')
iris = np.genfromtxt(url, delimiter=',', dtype=None, names=names, encoding='utf-8')

# Отримаємо унікальні імена видів для легенди та осі X
species_names = np.unique(iris['species'])
# ['Iris-setosa', 'Iris-versicolor', 'Iris-virginica']

# === 2. Налаштування сітки графіків ===
# Створюємо фігуру (figure) та набір осей (axes) розміром 2x2
# figsize=(12, 10) - робить загальне зображення більшим і читабельнішим
fig, ax = plt.subplots(2, 2, figsize=(12, 10))

# Додаємо загальний заголовок для всіх графіків
fig.suptitle('Аналіз набору даних "Іриси" Фішера', fontsize=16)
# === 3. Графік 1: Точкова діаграма (Scatter plot) ===
# Візуалізуємо Завдання 7 (фільтрація по видах)
# Порівнюємо довжину пелюстки (petallength) та ширину (petalwidth)
ax1 = ax[0, 0]
colors = ['red', 'green', 'blue']
markers = ['o', 's', '^'] # 'o' - коло, 's' - квадрат, '^' - трикутник

for i, s in enumerate(species_names):
    # Фільтруємо дані для кожного виду
    data = iris[iris['species'] == s]
    ax1.scatter(data['petallength'], data['petalwidth'],
                c=colors[i],       # колір
                marker=markers[i], # форма точки
                label=s,           # текст для легенди
                alpha=0.7)         # прозорість

ax1.set_title('Довжина vs Ширина Пелюстки')
ax1.set_xlabel('Довжина пелюстки (cm)')
ax1.set_ylabel('Ширина пелюстки (cm)')
ax1.legend() # показуємо легенду
ax1.grid(True) # додаємо сітку


# === 4. Графік 2: Гістограма (Histogram) ===
# Візуалізуємо Завдання 3 (середнє) та 6 (розподіл)
# Дивимось на розподіл довжини чашолистика (sepallength) для всіх квітів
ax2 = ax[0, 1]
ax2.hist(iris['sepallength'], bins=15, color='skyblue', edgecolor='black')

# Візуалізуємо середнє значення (з Завдання 3)
mean_val = np.mean(iris['sepallength'])
ax2.axvline(mean_val,
            color='red',
            linestyle='--',  # тип лінії: пунктир
            linewidth=2,
            label=f'Середнє: {mean_val:.2f} cm') # легенда для лінії

ax2.set_title('Розподіл Довжини Чашолистика')
ax2.set_xlabel('Довжина (cm)')
ax2.set_ylabel('Частота (кількість)')
ax2.legend()


# === 5. Графік 3: Стовпчаста діаграма (Bar chart) ===
# Візуалізуємо Завдання 8 (Середня довжина чашолистика для кожного виду)
ax3 = ax[1, 0]

# Розраховуємо середні значення
avg_lengths = []
for s in species_names:
    avg = np.mean(iris['sepallength'][iris['species'] == s])
    avg_lengths.append(avg)

# Створюємо простіші імена для осі X
clean_names = [s.replace('Iris-', '') for s in species_names]
bar_colors = ['#FF9999', '#66B2FF', '#99FF99'] # кастомні кольори

ax3.bar(clean_names, avg_lengths, color=bar_colors, edgecolor='black')
ax3.set_title('Середня Довжина Чашолистика (по Видах)')
ax3.set_ylabel('Середня довжина (cm)')


# === 6. Графік 4: Коробковий графік (Box plot) ===
# Візуалізуємо Завдання 4, 5 (мін, макс, медіана) для кожного виду
# Показує розподіл ширини чашолистика (sepalwidth)
ax4 = ax[1, 1]

# Готуємо дані: список з трьох масивів (по одному для кожного виду)
data_to_plot = []
for s in species_names:
    data_to_plot.append(iris['sepalwidth'][iris['species'] == s])

# patch_artist=True дозволяє нам розфарбувати "коробки"
bplot = ax4.boxplot(data_to_plot, labels=clean_names, patch_artist=True)

# Розфарбовуємо коробки в ті ж кольори, що і на графіку 3
for patch, color in zip(bplot['boxes'], bar_colors):
    patch.set_facecolor(color)

ax4.set_title('Розподіл Ширини Чашолистика (по Видах)')
ax4.set_ylabel('Ширина (cm)')
ax4.grid(True, axis='y') # сітка тільки по осі Y


# === 7. Фінальні налаштування та показ ===
# Автоматично налаштовує відступи, щоб елементи не накладались
plt.tight_layout(rect=[0, 0.03, 1, 0.95])

# Показати готовий графік
plt.show()