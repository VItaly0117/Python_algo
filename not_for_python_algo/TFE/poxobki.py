import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandas import DataFrame

# ЧАСТИНА 1. РОЗРАХУНОК KAPPA (ПОХИБКА ФОРМИ)
# Дані з таблиці в методичці (сторінка 10).
# Це вимірювання для "Інвертор + Лампа".
t_ms = np.array([0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20])
u_inv = np.array([0, 190, 295, 270, 150, -10, -185, -280, -275, -160, -5])

# Переведення часу в секунди
t_sec = t_ms / 1000.0

# Ідеальна синусоїда (310В, 50Гц -> omega=314.16)
omega = 314.16
u_ideal = 310 * np.sin(omega * t_sec)

# Метод найменших квадратів
epsilon_sq = (u_inv - u_ideal) ** 2
kappa = np.sqrt(np.mean(epsilon_sq))

# Формування таблиці для звіту
df_kappa: DataFrame = pd.DataFrame({
    't (мс)': t_ms,
    'U_inv (В)': u_inv,
    'U_ideal (В)': np.round(u_ideal, 2),
    'Epsilon^2': np.round(epsilon_sq, 2)
})

print(" 1. АНАЛІЗ ФОРМИ СИГНАЛУ (МЕТОД НАЙМЕНШИХ КВАДРАТІВ) ")
print(df_kappa.to_string(index=False))
print(f"\n>> Середньоквадратичне відхилення (Kappa): {kappa:.2f} В")
print("=" * 60 + "\n")
# ЧАСТИНА 2. КЛАСИЧНІ ПОХИБКИ ВИМІРЮВАННЯ
# Тут ми рахуємо похибки для ВСІХ випадків (Лампа і Кип'ятильник)
# Константи з налаштувань осцилографа:
K_VOLT = 50.0  # В/под [cite: 132]
K_TIME = 5.0  # мс/под [cite: 138]
DELTA_N = 0.2  # Абсолютна похибка зчитування (под.)


def analyze_measurement(name, n_amp, n_per):
    # 1. Амплітуда
    Um = n_amp * K_VOLT
    dUm = DELTA_N * K_VOLT
    eps_U = (dUm / Um) * 100

    # 2. Період
    T_ms = n_per * K_TIME
    dT_ms = DELTA_N * K_TIME
    eps_T = (dT_ms / T_ms) * 100

    # 3. Частота (f = 1/T)
    # eps_f (відносна) така ж, як eps_T
    f_hz = 1000 / T_ms
    df_hz = f_hz * (eps_T / 100)

    print(f"--- {name} ---")
    print(f"  Амплітуда (Um): {Um:.1f} ± {dUm:.1f} В (ε = {eps_U:.1f}%)")
    print(f"  Період (T):     {T_ms:.1f} ± {dT_ms:.1f} мс (ε = {eps_T:.1f}%)")
    print(f"  Частота (f):    {f_hz:.1f} ± {df_hz:.1f} Гц")
    print("-" * 40)

print(" 2. РЕЗУЛЬТАТИ ВИМІРЮВАНЬ ТА ПОХИБКИ ")

# --- ДАНІ З МЕТОДИЧКИ (Лампа і Кип'ятильник) ---

# 1. РОЗЕТКА (Мережа)
# Лампа: Nam=6.2, Nper=4 [cite: 131, 137]
analyze_measurement("РОЗЕТКА: Лампа", n_amp=6.2, n_per=4.0)

# Кип'ятильник: Nam=6.1, Nper=4 [cite: 131, 137]
analyze_measurement("РОЗЕТКА: Кип'ятильник", n_amp=6.1, n_per=4.0)

# 2. ІНВЕРТОР
# Лампа: Nam=6.3, Nper=4.1 [cite: 152, 153]
analyze_measurement("ІНВЕРТОР: Лампа", n_amp=6.3, n_per=4.1)

# Кип'ятильник: Nam=6.0, Nper=4.1 [cite: 152, 153]
analyze_measurement("ІНВЕРТОР: Кип'ятильник", n_amp=6.0, n_per=4.1)


# ЧАСТИНА 3. ГРАФІК (ВІЗУАЛІЗАЦІЯ)
plt.figure(figsize=(10, 6))

# Будуємо ідеальну синусоїду
plt.plot(t_ms, u_ideal, label='Ідеальна синусоїда (Розетка)', color='green', linestyle='--', linewidth=2)

# Будуємо точки інвертора (Лампа)
plt.plot(t_ms, u_inv, label='Сигнал Інвертора (Лампа)', color='red', marker='o', markersize=8)

# Коридор похибки Kappa
plt.fill_between(t_ms, u_ideal - kappa, u_ideal + kappa, color='gray', alpha=0.2,
                 label=f'Відхилення Kappa (±{kappa:.1f}В)')

plt.title(f'Порівняння форми сигналу (Kappa = {kappa:.2f} В)')
plt.xlabel('Час (мс)')
plt.ylabel('Напруга (В)')
plt.axhline(0, color='black', linewidth=0.8)
plt.axvline(0, color='black', linewidth=0.8)
plt.legend()
plt.grid(True, which='both', linestyle='--', alpha=0.7)
plt.tight_layout()

plt.savefig('lab_results.png')
plt.show()