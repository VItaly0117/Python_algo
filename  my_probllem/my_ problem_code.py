import matplotlib.pyplot as plt
import numpy as np


def draw_and_count_custom_lines(num_lines, line_length, line_spacing, direction='horizontal'):
    """
    Малює задану кількість ліній заданої довжини з певним інтервалом
    та підраховує їх.

    :param num_lines: Кількість ліній для малювання.
    :param line_length: Довжина кожної лінії.
    :param line_spacing: Відстань між центрами ліній.
    :param direction: Напрямок ліній ('horizontal' або 'vertical').
    :return: Загальна кількість намальованих ліній.
    """
    if num_lines <= 0:
        print("Кількість ліній повинна бути позитивним числом.")
        return 0

    fig, ax = plt.subplots(figsize=(10, 6))

    drawn_lines_count = 0

    # Визначимо початкову координату
    start_coord = 0

    for i in range(num_lines):
        # Координата початку лінії
        current_offset = start_coord + i * line_spacing

        if direction == 'horizontal':
            # Лінія йде по осі X, змінюється Y
            x_coords = [0, line_length]
            y_coords = [current_offset, current_offset]
            ax.plot(x_coords, y_coords, color='blue', linewidth=2)
        elif direction == 'vertical':
            # Лінія йде по осі Y, змінюється X
            x_coords = [current_offset, current_offset]
            y_coords = [0, line_length]
            ax.plot(x_coords, y_coords, color='red', linewidth=2)
        else:
            print(f"Невідомий напрямок: {direction}. Використовуємо 'horizontal'.")
            x_coords = [0, line_length]
            y_coords = [current_offset, current_offset]
            ax.plot(x_coords, y_coords, color='blue', linewidth=2)

        drawn_lines_count += 1

    # Налаштування вигляду графіка
    if direction == 'horizontal':
        ax.set_xlim(-line_length * 0.1, line_length * 1.1)
        ax.set_ylim(-line_spacing * 0.1, num_lines * line_spacing + line_spacing * 0.1)
        ax.set_xlabel('Довжина лінії')
        ax.set_ylabel('Позиція лінії')
    elif direction == 'vertical':
        ax.set_xlim(-line_spacing * 0.1, num_lines * line_spacing + line_spacing * 0.1)
        ax.set_ylim(-line_length * 0.1, line_length * 1.1)
        ax.set_xlabel('Позиція лінії')
        ax.set_ylabel('Довжина лінії')

    ax.set_title(f'Намальовано {drawn_lines_count} {direction} ліній')
    ax.grid(True)
    ax.set_aspect('equal', adjustable='box')  # Зробить одиниці по осях однаковими
    plt.show()

    return drawn_lines_count


# --- Приклади використання ---

# 1. Горизонтальні лінії
print("--- Горизонтальні лінії ---")
lines_h = draw_and_count_custom_lines(
    num_lines=7,  # Кількість ліній
    line_length=10,  # Довжина кожної лінії
    line_spacing=1.5,  # Відстань між лініями
    direction='horizontal'
)
print(f"Підраховано: {lines_h} горизонтальних ліній.")
print("\n")

# 2. Вертикальні лінії
print("--- Вертикальні лінії ---")
lines_v = draw_and_count_custom_lines(
    num_lines=5,  # Кількість ліній
    line_length=8,  # Довжина кожної лінії
    line_spacing=2,  # Відстань між лініями
    direction='vertical'
)
print(f"Підраховано: {lines_v} вертикальних ліній.")
print("\n")

# 3. Багато ліній, менший інтервал
print("--- Багато ліній, менший інтервал ---")
lines_many = draw_and_count_custom_lines(
    num_lines=20,  # Кількість ліній
    line_length=5,  # Довжина кожної лінії
    line_spacing=0.5,  # Відстань між лініями
    direction='horizontal'
)
print(f"Підраховано: {lines_many} горизонтальних ліній.")
print("\n")