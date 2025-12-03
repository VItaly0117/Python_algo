# ----------------------------------------------------------------- #
#                         IMPORTS & SETUP                           #
# ----------------------------------------------------------------- #
import numpy as np
from vpython import *
import csv
import datetime
import random

# ###################################################################
# #    M O L E C U L A R   D Y N A M I C S   (HYBRID EDITION)       #
# #    - Вид: Классический VPython (Красные/Белые)                  #
# #    - Ядро: NumPy (Быстрое)                                      #
# #    - Физика: С учетом массы (F = ma)                            #
# ###################################################################

# --- 1. НАСТРОЙКИ ЧАСТИЦ ---

# Типы: 0 = Тяжелые, 1 = Легкие
# Массы: Тяжелые в 4 раза тяжелее легких
mass_types = {0: 4.0, 1: 1.0}

# Матрица Силы (Epsilon) - глубина "ямы" притяжения
epsilon_matrix = np.array([
    [1.5, 1.0],  # [Тяж-Тяж, Тяж-Лег]
    [1.0, 0.5]  # [Лег-Тяж, Лег-Лег]
])

# Матрица Размера (Sigma) - радиус частицы
sigma_matrix = np.array([
    [1.0, 0.9],
    [0.9, 0.8]
])


# --- 2. ФИЗИЧЕСКОЕ ЯДРО (NUMPY) ---

def initialize_system(N, L, T, particle_types, mass_types):
    # Спавн внутри куба с отступом
    positions = (L - 2.0) * (np.random.rand(N, 3) - 0.5)

    velocities = np.zeros((N, 3))
    masses = np.array([mass_types[t] for t in particle_types])

    # Инициализация скоростей с учетом массы!
    # v ~ sqrt(T / m). Тяжелые будут медленнее.
    for i in range(N):
        sigma_v = np.sqrt(T / masses[i])
        velocities[i] = np.random.randn(3) * sigma_v

    velocities -= np.mean(velocities, axis=0)  # Убираем дрейф всей системы
    return positions, velocities, masses


def precompute_interaction_matrices(N, particle_types, epsilon_matrix, sigma_matrix):
    """Создаем карты взаимодействий (NxN) для NumPy"""
    eps_mat = np.zeros((N, N))
    sig_mat = np.zeros((N, N))
    for i in range(N):
        for j in range(N):
            t_i, t_j = particle_types[i], particle_types[j]
            eps_mat[i, j] = epsilon_matrix[t_i, t_j]
            sig_mat[i, j] = sigma_matrix[t_i, t_j]
    return eps_mat, sig_mat


def calculate_forces_vectorized(positions, L, r_cutoff_sq, eps_mat, sig_mat):
    """
    Супер-быстрый расчет сил на матрицах.
    Учитывает разные типы частиц через eps_mat и sig_mat.
    """
    N = len(positions)

    # 1. Векторы расстояний (NxNx3)
    r_vec = positions[:, np.newaxis, :] - positions[np.newaxis, :, :]

    # 2. Квадраты расстояний
    r_sq = np.sum(r_vec ** 2, axis=2)
    np.fill_diagonal(r_sq, np.inf)  # Игнорируем i==j

    mask = r_sq < r_cutoff_sq

    # 3. Расчет Леннард-Джонса
    r2_inv = np.zeros_like(r_sq)
    r2_inv[mask] = 1.0 / r_sq[mask]

    # Используем матрицы параметров для каждой пары
    sig2_r2 = (sig_mat[mask] ** 2) * r2_inv[mask]
    sig6_r6 = sig2_r2 ** 3
    sig12_r12 = sig6_r6 ** 2

    # Сила (скалярная часть)
    f_scal = np.zeros_like(r_sq)
    f_scal[mask] = 24.0 * eps_mat[mask] * (2.0 * sig12_r12 - sig6_r6) * r2_inv[mask]

    # Итоговая сила F = f_scal * вектор_r
    forces = np.sum(f_scal[:, :, np.newaxis] * r_vec, axis=1)

    # Энергия
    u_pot = 0.0
    if np.any(mask):
        u_pot = 2.0 * np.sum(eps_mat[mask] * (sig12_r12 - sig6_r6))

    return forces, u_pot


def berendsen_thermostat(velocities, T_desired, T_current, dt, tau=0.5):
    """Мягкий контроль температуры"""
    if T_current > 0:
        scale = np.sqrt(1 + (dt / tau) * (T_desired / T_current - 1))
        velocities *= scale
    return velocities


# --- 3. ПАРАМЕТРЫ ЗАПУСКА ---

N = 80  # Кол-во частиц (оптимально для красивой картинки)
L = 18.0  # Размер куба
T = 2.0  # Температура
dt = 0.001  # Шаг времени (точность)
r_cutoff = 4.0
particle_ratio = 0.5  # 50% Тяжелых, 50% Легких

# Логирование
RUN_ID = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
CSV_FILENAME = f"md_hybrid_log_{RUN_ID}.csv"

# --- 4. ИНИЦИАЛИЗАЦИЯ СИСТЕМЫ ---

# Генерируем типы
particle_types = np.array([0 if random.random() < particle_ratio else 1 for _ in range(N)])
# Готовим матрицы для NumPy
eps_mat, sig_mat = precompute_interaction_matrices(N, particle_types, epsilon_matrix, sigma_matrix)
# Создаем частицы
positions, velocities, masses = initialize_system(N, L, T, particle_types, mass_types)
accelerations = np.zeros_like(positions)

# --- 5. ВИЗУАЛИЗАЦИЯ (VPYTHON - КЛАССИКА) ---

scene = canvas(title='<b>MD SIMULATION: Mass + NumPy + Graphs</b>',
               width=1000, height=500, center=vec(0, 0, 0), background=color.black)

# Стенки куба (голубоватый каркас)
box(pos=vec(0, 0, 0), size=vec(L, L, L), opacity=0.1, color=color.cyan)

# Создаем шарики
visual_particles = []
for i in range(N):
    t = particle_types[i]
    if t == 0:  # ТЯЖЕЛЫЕ
        col = color.red
        rad = 0.65
    else:  # ЛЕГКИЕ
        col = color.white
        rad = 0.4

    # emissive=True делает их "светящимися" (как ты просил неон)
    p = sphere(pos=vec(0, 0, 0), radius=rad, color=col, opacity=0.9, emissive=True)
    visual_particles.append(p)

# --- ДИАГРАММЫ (ВЕРНУЛИ НА МЕСТО!) ---
scene.append_to_caption('\n\n')

# 1. График Энергии
g_energy = graph(width=600, height=250, title='Energy Balance (Real-time)', xtitle='Step', ytitle='Energy')
plot_ek = gcurve(graph=g_energy, color=color.orange, label='Kinetic')
plot_ep = gcurve(graph=g_energy, color=color.blue, label='Potential')
plot_et = gcurve(graph=g_energy, color=color.white, label='Total')

# 2. Гистограмма Скоростей
scene.append_to_caption('\n')
g_hist = graph(width=600, height=200, title='Speed Distribution (Maxwell)', xtitle='Speed v', ytitle='Count')
hist_bars = gvbars(graph=g_hist, color=color.green, delta=0.2)

# CSV Writer
csv_file = open(CSV_FILENAME, 'w', newline='', encoding='utf-8')
writer = csv.writer(csv_file)
writer.writerow(["Step", "Kinetic", "Potential", "Total", "Temperature"])

# --- 6. ГЛАВНЫЙ ЦИКЛ ---

step = 0
print(f"🚀 HYBRID SIMULATION STARTED!")
print(f"🔴 Heavy Mass: {mass_types[0]} | ⚪ Light Mass: {mass_types[1]}")

PHYSICS_STEPS = 4  # Считаем 4 раза физику перед 1 перерисовкой (чтобы было плавно)

while True:
    rate(60)  # Ограничиваем FPS экрана, чтобы не мерцало

    for _ in range(PHYSICS_STEPS):
        # --- A. Интегратор Верле (Шаг 1) ---
        velocities += 0.5 * accelerations * dt
        positions += velocities * dt

        # --- B. Отскок от стенок (Граничные условия) ---
        for k in range(3):  # Проход по x, y, z
            # Удар справа/сверху/спереди
            hit_plus = positions[:, k] > L / 2
            positions[hit_plus, k] = L / 2
            velocities[hit_plus, k] *= -1

            # Удар слева/снизу/сзади
            hit_minus = positions[:, k] < -L / 2
            positions[hit_minus, k] = -L / 2
            velocities[hit_minus, k] *= -1

        # --- C. Расчет Сил (NumPy Matrix Magic) ---
        forces, ep = calculate_forces_vectorized(positions, L, r_cutoff ** 2, eps_mat, sig_mat)

        # --- D. Второй закон Ньютона (a = F / m) ---
        # ВАЖНО: Делим силу на массу! Тяжелые ускоряются хуже.
        accelerations = forces / masses[:, np.newaxis]

        # --- E. Интегратор Верле (Шаг 2) ---
        velocities += 0.5 * accelerations * dt

        # --- F. Термостат и Температура ---
        # Ek = 0.5 * m * v^2 (Учитываем массу!)
        v_sq = np.sum(velocities ** 2, axis=1)
        ek = 0.5 * np.sum(masses * v_sq)

        curr_T = (2.0 * ek) / (3.0 * N)
        velocities = berendsen_thermostat(velocities, T, curr_T, dt)

    step += PHYSICS_STEPS

    # --- ВИЗУАЛИЗАЦИЯ ---
    for i in range(N):
        visual_particles[i].pos = vec(*positions[i])

    # --- ОБНОВЛЕНИЕ ГРАФИКОВ (Раз в 40 шагов) ---
    if step % 40 == 0:
        et = ek + ep

        # Рисуем кривые
        plot_ek.plot(step, ek)
        plot_ep.plot(step, ep)
        plot_et.plot(step, et)

        # Рисуем гистограмму
        speeds = np.linalg.norm(velocities, axis=1)
        counts, bins = np.histogram(speeds, bins=15, range=(0, np.max(speeds) * 1.1))

        # Обновляем столбики
        data = []
        for i in range(len(counts)):
            data.append([bins[i], counts[i]])
        hist_bars.data = data

        # Пишем в CSV
        writer.writerow([step, ek, ep, et, curr_T])

        # Инфо под графиками
        scene.caption = f"""
        <b>Step:</b> {step}
        <b>Particles:</b> {N}
        <b>Temp:</b> {curr_T:.2f} / {T}
        <b>Total E:</b> {et:.2f}
        """