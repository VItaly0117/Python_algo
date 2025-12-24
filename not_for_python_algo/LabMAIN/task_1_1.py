import numpy as np
import matplotlib.pyplot as plt
import stats_lib as sl

data_millikan = [
    4.781, 4.764, 4.777, 4.809, 4.761, 4.769, 4.772, 4.764,
    4.795, 4.776, 4.765, 4.790, 4.792, 4.806, 4.785, 4.788,
    4.769, 4.771, 4.785, 4.779, 4.758, 4.779, 4.799, 4.749,
    4.792, 4.789, 4.805, 4.788, 4.764, 4.785, 4.791, 4.774,
    4.779, 4.772, 4.768, 4.772, 4.810, 4.790, 4.783, 4.783,
    4.775, 4.789, 4.801, 4.791, 4.799, 4.777, 4.797, 4.781,
    4.782, 4.778, 4.808, 4.740, 4.790, 4.767, 4.791, 4.771,
    4.775, 4.747
]


def run_task():
    print("--- ЗАВДАННЯ 1.1 (Дослід Міллікена) ---")
    data = np.array(data_millikan)
    n = len(data)
    alpha = 0.99

    mean_val, var, std, std_err = sl.calculate_basics(data)
    delta, t_val = sl.get_confidence_interval(mean_val, std_err, n, alpha)

    print(f"Кількість вимірювань (n): {n}")
    print(f"Вибіркове середнє (Xsr): {mean_val:.3f}")
    print(f"Вибіркова дисперсія (S^2): {var:}")
    print(f"Середньоквадратичне відхилення (Sx): {std:.3f}")
    print(f"Середньоквадратична похибка (Sigma X): {std_err:.3f}")
    print(f"Коефіцієнт Стьюдента (t) для a={alpha}: {t_val:.3f}")
    print(f"Довірчий інтервал (Delta X): {delta:.3f}")
    print(f"Результат: ({mean_val:.3f} ± {delta:.3f}) * 10^-10 од. СГСЕ")

    cgse_to_coulomb = 3.33564e-10
    factor = 1e-10

    mean_si = mean_val * factor * cgse_to_coulomb
    delta_si = delta * factor * cgse_to_coulomb

    print(f"\nУ системі СІ: ({mean_si:.3e} ± {delta_si:.3e}) Кл")

    plt.figure(figsize=(10, 6))
    count, bins, ignored = plt.hist(data, bins=10, density=True, alpha=0.6, color='g', edgecolor='black',
                                    label='Експеримент')

    xmin, xmax = plt.xlim()
    x = np.linspace(xmin, xmax, 100)
    p = sl.gaussian_func(x, mean_val, std)
    plt.plot(x, p, 'k', linewidth=2, label='Нормальний закон')

    plt.title('Гістограма розподілу заряду (Завдання 1.1)')
    plt.xlabel('Заряд (од. * 10^-10)')
    plt.ylabel('Густина ймовірності')
    plt.legend()
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    run_task()