# 1. Импортируем необходимые библиотеки
import pandas as pd
import matplotlib.pyplot as plt

# 2. Создаем вымышленные данные
data = {
    'month': ['Січ', 'Лют', 'Бер', 'Кві', 'Тра', 'Чер', 'Лип', 'Сер', 'Вер', 'Жов', 'Лис', 'Гру'],
    'temperature': [-5.6, -4.2, 1.1, 9.2, 15.5, 18.6, 20.5, 19.8, 14.2, 8.1, 2.1, -2.9]
}
df = pd.DataFrame(data)

# 3. Создаем "полотно" и сетку для двух графиков
fig, ax = plt.subplots(2, 1, figsize=(12, 10))

# --- График 1: Линейный график (без изменений) ---
ax[0].plot(
    df['month'],
    df['temperature'],
    marker='o',
    linestyle='--',
    color='dodgerblue',
    label='Середня температура'
)
ax[0].set_title('Динаміка середньомісячної температури', fontsize=14)
ax[0].set_ylabel('Температура (°C)')
ax[0].grid(True, linestyle=':', alpha=0.7)
ax[0].legend()

# --- График 2: Столбчатая диаграмма (ИЗМЕНЕНИЕ ЗДЕСЬ) ---
# Вместо сложной генерации цветов, используем один простой цвет
ax[1].bar(df['month'], df['temperature'], color='skyblue') # <-- ИЗМЕНЕННАЯ СТРОКА
ax[1].set_title('Порівняння температури по місяцях', fontsize=14)
ax[1].set_ylabel('Температура (°C)')

# 4. Финальные штрихи
fig.suptitle('Аналіз вигаданих погодних даних для Києва', fontsize=18)
plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.show()