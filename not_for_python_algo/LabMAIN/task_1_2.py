import numpy as np
import stats_lib as sl

voltage_data = [210, 205, 195, 200, 210, 220, 190, 210]


def run_task():
    print("\n--- ЗАВДАННЯ 1.2 (Напруга в електромережі) ---")
    data = np.array(voltage_data)
    n = len(data)

    mean_val, var, std, std_err = sl.calculate_basics(data)

    print(f"Середня напруга (Xsr): {mean_val} В")
    print(f"Дисперсія (S^2): {var:.2f}")
    print(f"Середньоквадратичне відхилення (Sx): {std:.2f}")
    print(f"Середньоквадратична похибка (Sigma X): {std_err:.2f}")

    alphas = [0.95, 0.99]
    for a in alphas:
        delta, t_val = sl.get_confidence_interval(mean_val, std_err, n, a)
        low = mean_val - delta
        high = mean_val + delta
        print(f"Для a={a}: t={t_val:.3f}, Delta={delta:.2f} => Інтервал: [{low:.2f}; {high:.2f}] В")


if __name__ == "__main__":
    run_task()