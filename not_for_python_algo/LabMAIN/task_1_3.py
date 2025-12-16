import numpy as np
from scipy import stats
import stats_lib as sl

temp_x = [0, 50, 100, 150, 200, 300, 400, 500, 600, 700]
strength_y = [23.3, 21.0, 19.2, 16.4, 15.5, 13.3, 9.4, 5.9, 4.1, 1.9]


def check_significance(r, n):
    if abs(r) >= 1.0:
        return "Функціональний зв'язок (r=1)", 1.0

    df = n - 2
    t_obs = abs(r) * np.sqrt(df / (1 - r ** 2))

    print(f"\n--- Перевірка значущості (t-критерій) ---")
    print(f"Ступені свободи (df = n-2): {df}")
    print(f"Розрахункове значення t-статистики: {t_obs:.4f}")

    thresholds = [0.999, 0.99, 0.95]
    found_reliability = None

    for alpha in thresholds:
        t_crit = stats.t.ppf((1 + alpha) / 2, df)
        print(f"  Критичне t для P={alpha}: {t_crit:.4f}")

        if t_obs > t_crit:
            if found_reliability is None:
                found_reliability = alpha

    return t_obs, found_reliability


def run_task():
    print("\n--- ЗАВДАННЯ 1.3 (Кореляційний аналіз) ---")

    n = len(temp_x)

    mx, vx, sx, ex = sl.calculate_basics(np.array(temp_x))
    my, vy, sy, ey = sl.calculate_basics(np.array(strength_y))

    print("Характеристики X (Температура):")
    print(f"  Середнє (Xsr): {mx}, Дисперсія: {vx:.2f}, Sx: {sx:.2f}, SigmaX: {ex:.2f}")

    print("Характеристики Y (Міцність):")
    print(f"  Середнє (Ysr): {my}, Дисперсія: {vy:.2f}, Sy: {sy:.2f}, SigmaY: {ey:.2f}")

    r = sl.calculate_correlation(temp_x, strength_y)
    print(f"\nКоефіцієнт кореляції r: {r:.4f}")

    if abs(r) > 0.9:
        print("Сила зв'язку: Дуже сильна.")
    elif abs(r) > 0.7:
        print("Сила зв'язку: Сильна.")
    elif abs(r) > 0.5:
        print("Сила зв'язку: Помірна.")
    else:
        print("Сила зв'язку: Слабка.")

    if r < 0:
        print("Напрямок: Зворотний (зі зростанням температури міцність падає).")

    t_stat, reliability = check_significance(r, n)

    print("\nВИСНОВОК ПРО ДОСТОВІРНІСТЬ:")
    if reliability:
        print(f"Зв'язок є статистично значущим з надійністю P > {reliability} (Поріг достовірності).")
    else:
        print("Зв'язок статистично незначущий (надійність P < 0.95).")


if __name__ == "__main__":
    run_task()