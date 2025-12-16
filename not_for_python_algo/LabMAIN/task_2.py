import numpy as np
import matplotlib.pyplot as plt
import stats_lib as sl
from scipy.integrate import quad


def run_task():
    print("\n--- ЗАВДАННЯ 2 (Графіки Гауса) ---")

    mu = 10
    sigmas = [1, 3, 6]
    colors = ['r', 'g', 'b']

    x = np.linspace(mu - 20, mu + 20, 1000)

    plt.figure(figsize=(10, 6))

    for sigma, color in zip(sigmas, colors):
        y = sl.gaussian_func(x, mu, sigma)
        plt.plot(x, y, color=color, label=f'sigma = {sigma}')

        area, _ = quad(sl.gaussian_func, -np.inf, np.inf, args=(mu, sigma))
        print(f"Площа під кривою (sigma={sigma}): {area:.5f}")

    plt.title('Сімейство кривих Гауса')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.legend()
    plt.grid(True)
    plt.show()

    print("Висновок: Зі збільшенням сигми графік стає ширшим і нижчим, але площа завжди дорівнює ~1.")


if __name__ == "__main__":
    run_task()