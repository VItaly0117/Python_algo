import matplotlib.pyplot as plt
from matplotlib.widgets import Slider


# Ваша функція для малювання трикутника залишилася без змін
def draw_sierpinski(ax, x1, y1, x2, y2, x3, y3, level):
    """Рекурсивно малює трикутник Серпінського на вказаних осях (ax)."""
    if level == 0:
        ax.fill([x1, x2, x3], [y1, y2, y3], 'blue')
        return

    # Знаходимо середні точки сторін
    x12 = (x1 + x2) / 2
    y12 = (y1 + y2) / 2
    x23 = (x2 + x3) / 2
    y23 = (y2 + y3) / 2
    x31 = (x3 + x1) / 2
    y31 = (y3 + y1) / 2

    # Рекурсивно викликаємо функцію для трьох менших трикутників
    draw_sierpinski(ax, x1, y1, x12, y12, x31, y31, level - 1)
    draw_sierpinski(ax, x12, y12, x2, y2, x23, y23, level - 1)
    draw_sierpinski(ax, x31, y31, x23, y23, x3, y3, level - 1)


# --- Налаштування інтерактивного вікна ---

# Створюємо фігуру та осі для графіка
fig, ax = plt.subplots(figsize=(8, 8))
plt.subplots_adjust(bottom=0.2)  # Залишаємо місце знизу для слайдера

# Початкові координати основного трикутника
initial_coords = [0, 1, -1, -0.5, 1, -0.5]
initial_level = 0

# Налаштування осей
ax.set_aspect('equal')
ax.axis('off')

# Створюємо вісь для слайдера [left, bottom, width, height]
ax_slider = fig.add_axes([0.2, 0.1, 0.65, 0.03])

# Створюємо сам слайдер
slider = Slider(
    ax=ax_slider,
    label='Глибина',
    valmin=0,  # Мінімальна глибина
    valmax=8,  # Максимальна глибина
    valinit=initial_level,  # Початкове значення
    valstep=1  # Крок зміни (цілі числа)
)


# Функція, яка буде викликатися при зміні значення слайдера
def update(val):
    level = int(slider.val)  # Отримуємо нове значення глибини
    ax.clear()  # Очищуємо попередній малюнок
    ax.axis('off')  # Вимикаємо осі знову, бо clear() їх вмикає
    ax.set_aspect('equal')
    # Малюємо фрактал з новою глибиною
    draw_sierpinski(ax, *initial_coords, level=level)
    fig.canvas.draw_idle()  # Оновлюємо вікно графіка


# "Підключаємо" нашу функцію update до слайдера
slider.on_changed(update)

# Малюємо початковий стан
update(initial_level)

plt.show()