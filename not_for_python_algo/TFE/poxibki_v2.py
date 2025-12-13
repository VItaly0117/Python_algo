import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandas import DataFrame

print("=" * 70)
print("ЛАБОРАТОРНА РОБОТА: ВИВЧЕННЯ ОСЦИЛОГРАФА ТА ВИМІРЮВАННЯ ПАРАМЕТРІВ СИГНАЛІВ")
print("=" * 70 + "\n")

# ЧАСТИНА 1. РОЗРАХУНОК KAPPA (ПОХИБКА ФОРМИ) - ІНВЕРТОР + ЛАМПА
print("ЧАСТИНА 1. АНАЛІЗ ФОРМИ СИГНАЛУ (МЕТОД НАЙМЕНШИХ КВАДРАТІВ)")
print("-" * 70)

t_ms = np.array([0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20])
u_inv = np.array([0, 190, 295, 270, 150, -10, -185, -280, -275, -160, -5])

t_sec = t_ms / 1000.0
omega = 314.16
u_ideal = 310 * np.sin(omega * t_sec)

# Розрахунок похибок
epsilon = u_inv - u_ideal
epsilon_sq = epsilon ** 2
kappa = np.sqrt(np.mean(epsilon_sq))

# Додаткові статистики
max_error = np.max(np.abs(epsilon))
relative_kappa = (kappa / 310) * 100  # Відсоток від амплітуди

# Формування таблиці для звіту
df_kappa = pd.DataFrame({
    't (мс)': t_ms,
    'U_inv (В)': u_inv,
    'U_ideal (В)': np.round(u_ideal, 2),
    'ε (В)': np.round(epsilon, 2),
    'ε² (В²)': np.round(epsilon_sq, 2)
})

print(df_kappa.to_string(index=False))
print(f"\nСТАТИСТИКА ПОХИБОК:")
print(f"  • Середньоквадратичне відхилення (Kappa): {kappa:.2f} В")
print(f"  • Відносна похибка форми: {relative_kappa:.1f}% від амплітуди")
print(f"  • Максимальна абсолютна похибка: {max_error:.1f} В")
print(f"  • Середня абсолютна похибка: {np.mean(np.abs(epsilon)):.1f} В")
print("=" * 70 + "\n")

# ЧАСТИНА 2. КЛАСИЧНІ ПОХИБКИ ВИМІРЮВАНЬ
print("ЧАСТИНА 2. РЕЗУЛЬТАТИ ВИМІРЮВАНЬ ТА ПОХИБКИ")
print("-" * 70)

# Константи
K_VOLT = 50.0  # В/под
K_TIME = 5.0  # мс/под
DELTA_N = 0.2  # похибка зчитування (под.)


def analyze_measurement(name, n_amp, n_per):
    """Розрахунок параметрів сигналу з похибками"""
    # Амплітуда
    Um = n_amp * K_VOLT
    dUm = DELTA_N * K_VOLT
    eps_U = (dUm / Um) * 100

    # Діюча напруга
    Ud = Um / np.sqrt(2)
    dUd = dUm / np.sqrt(2)
    eps_Ud = (dUd / Ud) * 100

    # Період
    T_ms = n_per * K_TIME
    dT_ms = DELTA_N * K_TIME
    eps_T = (dT_ms / T_ms) * 100

    # Частота
    f_hz = 1000 / T_ms  # переведення мс у с
    # Похідна для похибки частоти: df = |∂f/∂T| * dT = (1000/T²) * dT
    df_hz = (1000 / T_ms ** 2) * dT_ms
    eps_f = (df_hz / f_hz) * 100

    # Кутова частота
    omega_rad = 2 * np.pi * f_hz

    return {
        'name': name,
        'Um': Um, 'dUm': dUm, 'eps_U': eps_U,
        'Ud': Ud, 'dUd': dUd, 'eps_Ud': eps_Ud,
        'T': T_ms, 'dT': dT_ms, 'eps_T': eps_T,
        'f': f_hz, 'df': df_hz, 'eps_f': eps_f,
        'omega': omega_rad
    }


# Дані з методички
measurements = [
    ("РОЗЕТКА: Лампа", 6.2, 4.0),
    ("РОЗЕТКА: Кип'ятильник", 6.1, 4.0),
    ("ІНВЕРТОР: Лампа", 6.3, 4.1),
    ("ІНВЕРТОР: Кип'ятильник", 6.0, 4.1)
]

results = []
for name, n_amp, n_per in measurements:
    res = analyze_measurement(name, n_amp, n_per)
    results.append(res)

    print(f"{name}")
    print(f"  Амплітуда:     {res['Um']:.1f} ± {res['dUm']:.1f} В (ε = {res['eps_U']:.1f}%)")
    print(f"  Діюча напруга: {res['Ud']:.1f} ± {res['dUd']:.1f} В (ε = {res['eps_Ud']:.1f}%)")
    print(f"  Період:        {res['T']:.1f} ± {res['dT']:.1f} мс (ε = {res['eps_T']:.1f}%)")
    print(f"  Частота:       {res['f']:.1f} ± {res['df']:.1f} Гц (ε = {res['eps_f']:.1f}%)")
    print(f"  Кут. частота:  {res['omega']:.1f} рад/с")
    print("-" * 50)

# Створення зведеної таблиці
summary_data = []
for res in results:
    summary_data.append([
        res['name'],
        f"{res['Um']:.1f} ± {res['dUm']:.1f} В",
        f"{res['eps_U']:.1f}%",
        f"{res['Ud']:.1f} ± {res['dUd']:.1f} В",
        f"{res['eps_Ud']:.1f}%",
        f"{res['T']:.1f} ± {res['dT']:.1f} мс",
        f"{res['eps_T']:.1f}%",
        f"{res['f']:.1f} ± {res['df']:.1f} Гц",
        f"{res['eps_f']:.1f}%"
    ])

df_summary = pd.DataFrame(summary_data, columns=[
    'Джерело та навантаження',
    'Амплітуда (Um)',
    'ε_Um',
    'Діюча напруга (Ud)',
    'ε_Ud',
    'Період (T)',
    'ε_T',
    'Частота (f)',
    'ε_f'
])

print("\nЗВЕДЕНА ТАБЛИЦЯ РЕЗУЛЬТАТІВ:")
print(df_summary.to_string(index=False))
print("=" * 70 + "\n")

# ЧАСТИНА 3. АНАЛІЗ ФІГУР ЛІССАЖУ
print("ЧАСТИНА 3. АНАЛІЗ ФІГУР ЛІССАЖУ (ТЕОРЕТИЧНИЙ АНАЛІЗ)")
print("-" * 70)

print("Фігури Ліссажу утворюються при подачі двох синусоїдальних сигналів на:")
print("  • X (горизонталь): сигнал від розетки (50 Гц)")
print("  • Y (вертикаль): сигнал від інвертора (~48.8 Гц)")

print("\nОЧІКУВАНІ РЕЗУЛЬТАТИ:")
print("1. Для лампи (розетка vs інвертор):")
print("   • Частота розетки: 50.0 Гц")
print("   • Частота інвертора: 48.8 Гц")
print("   • Різниця частот: Δf = 1.2 Гц")
print("   • Фігура: повільно обертовий еліпс")
print("   • Період обертання: T_оберт = 1/Δf ≈ 0.83 с")

print("\n2. Для кип'ятильника:")
print("   • Інвертор не є 'чистою синусоїдою' → наявні вищі гармоніки")
print("   • Фігура буде складною, нестійкою")
print("   • Можливі форми: вигнута трапеція або 'метелик'")
print("   • Це свідчить про наявність гармонік у сигналі інвертора")

print("\nВИСНОВОК ЩОДО ФІГУР ЛІССАЖУ:")
print("• Обертання еліпса свідчить про малу різницю частот Δf")
print("• Чим повільніше обертання, тим краще інвертор тримає частоту 50 Гц")
print("• Складні форми фігур вказують на відхилення від ідеальної синусоїди")
print("=" * 70 + "\n")

# ЧАСТИНА 4. ГРАФІКИ
print("ЧАСТИНА 4. ВІЗУАЛІЗАЦІЯ РЕЗУЛЬТАТІВ")
print("-" * 70)

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('ПОРІВНЯЛЬНИЙ АНАЛІЗ СИГНАЛІВ', fontsize=16, fontweight='bold')

# Графік 1: Порівняння форми сигналу
ax1 = axes[0, 0]
ax1.plot(t_ms, u_ideal, label='Ідеальна синусоїда (Розетка)',
         color='green', linestyle='--', linewidth=2)
ax1.plot(t_ms, u_inv, label='Сигнал Інвертора (Лампа)',
         color='red', marker='o', markersize=6, linewidth=1.5)
ax1.fill_between(t_ms, u_ideal - kappa, u_ideal + kappa,
                 color='gray', alpha=0.2, label=f'Похибка Kappa (±{kappa:.1f}В)')
ax1.set_title(f'Порівняння форми сигналу (Kappa = {kappa:.2f} В)')
ax1.set_xlabel('Час (мс)')
ax1.set_ylabel('Напруга (В)')
ax1.grid(True, alpha=0.3)
ax1.legend()
ax1.axhline(0, color='black', linewidth=0.8)
ax1.axvline(0, color='black', linewidth=0.8)

# Графік 2: Похибка форми сигналу
ax2 = axes[0, 1]
bars = ax2.bar(t_ms, epsilon, width=1.5, color='steelblue', alpha=0.7)
ax2.set_title('Абсолютна похибка форми сигналу')
ax2.set_xlabel('Час (мс)')
ax2.set_ylabel('Похибка ε (В)')
ax2.grid(True, alpha=0.3, axis='y')
ax2.axhline(0, color='black', linewidth=0.8)

# Додаємо значення над стовпцями
for bar in bars:
    height = bar.get_height()
    ax2.text(bar.get_x() + bar.get_width() / 2., height + 3,
             f'{height:.0f}', ha='center', va='bottom', fontsize=8)

# Графік 3: Амплітуди сигналів
ax3 = axes[1, 0]
categories = [res['name'] for res in results]
um_values = [res['Um'] for res in results]
um_errors = [res['dUm'] for res in results]
colors = ['#2E8B57', '#3CB371', '#DC143C', '#FF6347']

bars3 = ax3.bar(categories, um_values, yerr=um_errors,
                capsize=5, alpha=0.8, color=colors, edgecolor='black')
ax3.set_title('Порівняння амплітудних значень напруги')
ax3.set_ylabel('Амплітуда Um (В)')
ax3.grid(True, alpha=0.3, axis='y')
ax3.tick_params(axis='x', rotation=15)

# Додаємо значення над стовпцями
for bar, val in zip(bars3, um_values):
    height = bar.get_height()
    ax3.text(bar.get_x() + bar.get_width() / 2., height + 5,
             f'{val:.0f} В', ha='center', va='bottom', fontweight='bold')

# Графік 4: Частоти сигналів
ax4 = axes[1, 1]
f_values = [res['f'] for res in results]
f_errors = [res['df'] for res in results]
ideal_f = [50, 50, 50, 50]  # Ідеальна частота

x_pos = np.arange(len(categories))
width = 0.35

bars4_ideal = ax4.bar(x_pos - width / 2, ideal_f, width,
                      label='Ідеал (50 Гц)', alpha=0.7, color='green')
bars4_meas = ax4.bar(x_pos + width / 2, f_values, width,
                     yerr=f_errors, capsize=3, label='Виміряне',
                     alpha=0.7, color='orange', edgecolor='black')

ax4.set_title('Порівняння частот сигналів')
ax4.set_ylabel('Частота f (Гц)')
ax4.set_xticks(x_pos)
ax4.set_xticklabels([cat.split(':')[0] for cat in categories])
ax4.grid(True, alpha=0.3, axis='y')
ax4.legend()

# Додаємо значення над стовпцями
for bar, val in zip(bars4_meas, f_values):
    height = bar.get_height()
    ax4.text(bar.get_x() + bar.get_width() / 2., height + 0.3,
             f'{val:.1f} Гц', ha='center', va='bottom', fontsize=9)

plt.tight_layout()
plt.savefig('lab_complete_results.png', dpi=300, bbox_inches='tight')
print("Графіки збережено у файл 'lab_complete_results.png'")
print("=" * 70 + "\n")

# ЧАСТИНА 5. ВИСНОВКИ
print("ЧАСТИНА 5. ЗАГАЛЬНІ ВИСНОВКИ")
print("-" * 70)

print("1. РОБОТА ОСЦИЛОГРАФА:")
print("   • Осцилограф дозволяє візуалізувати електричні сигнали")
print("   • Параметри 'Вольт/поділка' та 'Час/поділка' визначають масштаб")
print("   • Чутливість: вертикальна - 50 В/под, горизонтальна - 5 мс/под")

print("\n2. РЕЗУЛЬТАТИ ВИМІРЮВАНЬ:")
print("   • Розетка дає стабільну синусоїду 50 Гц")
print("   • Інвертор має незначне відхилення частоти (48.8 Гц)")
print("   • Форма сигналу інвертора відрізняється від ідеальної синусоїди")

print("\n3. ПОХИБКИ ВИМІРЮВАНЬ:")
print(f"   • Похибка форми (Kappa): {kappa:.1f} В ({relative_kappa:.1f}%)")
print("   • Похибка амплітуди: 3.2-3.3% (основна похибка - зчитування)")
print("   • Похибка періоду: 4.9-5.0%")
print("   • Похибка частоти: 4.8-5.0%")

print("\n4. ПОРІВНЯННЯ ДЖЕРЕЛ:")
print("   • Розетка: ідеальна синусоїда, стабільна частота 50 Гц")
print("   • Інвертор: 'модифікована синусоїда', частота ~48.8 Гц")
print("   • Навантаження мало впливає на параметри сигналу")

print("\n5. ФІГУРИ ЛІССАЖУ:")
print("   • Свідчать про незначну різницю частот між джерелами")
print("   • Підтверджують наявність гармонік у сигналі інвертора")

print("\n" + "=" * 70)
print("ЛАБОРАТОРНУ РОБОТУ ВИКОНАНО")
print("=" * 70)

# Додаткове збереження результатів у CSV
df_summary.to_csv('lab_results_summary.csv', index=False, encoding='utf-8-sig')
print("\nДані збережено у файли:")
print("  • lab_complete_results.png - графіки")
print("  • lab_results_summary.csv - таблиця результатів")

# Показати графіки
plt.show()