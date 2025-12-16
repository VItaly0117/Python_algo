import numpy as np
import stats_lib as sl

temp_x = [0, 50, 100, 150, 200, 300, 400, 500, 600, 700]
strength_y = [23.3, 21.0, 19.2, 16.4, 15.5, 13.3, 9.4, 5.9, 4.1, 1.9]


def run_task():
    print("\n--- ЗАВДАННЯ 1.3 (Кореляційний аналіз) ---")

    mx, vx, sx, ex = sl.calculate_basics(np.array(temp_x))
    my, vy, sy, ey = sl.calculate_basics(np.array(strength_y))

    print("Характеристики X (Температура):")
    print(f"  Середнє: {mx}, Дисперсія: {vx:.2f}, Sx: {sx:.2f}, SigmaX: {ex:.2f}")

    print("Характеристики Y (Міцність):")
    print(f"  Середнє: {my}, Дисперсія: {vy:.2f}, Sy: {sy:.2f}, SigmaY: {ey:.2f}")

    r = sl.calculate_correlation(temp_x, strength_y)
    print(f"Коефіцієнт кореляції r: {r:.4f}")

    if abs(r) > 0.9:
        print("Висновок: Дуже сильний лінійний зв'язок.")
    elif abs(r) > 0.7:
        print("Висновок: Сильний лінійний зв'язок.")

    if r < 0:
        print("Зв'язок обернений (зі зростанням температури міцність падає).")


if __name__ == "__main__":
    run_task()