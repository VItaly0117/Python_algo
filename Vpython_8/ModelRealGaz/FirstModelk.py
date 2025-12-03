# ----------------------------------------------------------------- #
#                         IMPORTS & SETUP                           #
# ----------------------------------------------------------------- #
import numpy as np
from vpython import *
from collections import deque
import csv
import datetime
import random


# ###################################################################
# #                                                                 #
# #    M O L E C U L A R   D Y N A M I C S   S I M U L A T O R      #
# #                                                                 #
# #    - v14 (MASS + EXPLANATIONS)                                  #
# #    - Теперь с массами и подробными комментариями!               #
# #                                                                 #
# ###################################################################

# --- 1. CORE PHYSICS FUNCTIONS ---

def initialize_system(N, L, T, particle_types, mass_types):
    """
    Инициализация системы:
    - positions: начальные позиции частиц (случайные в центре куба)
    - velocities: начальные скорости (случайные, но с нулевым суммарным импульсом)
    """
    positions = (L - 1.0) * (np.random.rand(N, 3) - 0.5)
    velocities = np.random.randn(N, 3) * np.sqrt(T)
    velocities = velocities - velocities.mean(axis=0)  # Убираем общее движение

    # Создаем массив масс для каждой частицы
    masses = np.array([mass_types[t] for t in particle_types])

    return positions, velocities, masses


def calculate_forces_multi(positions, L, r_cutoff_sq, particle_types, epsilon_matrix, sigma_matrix):
    """
    Расчет сил между ВСЕМИ парами частиц по потенциалу Леннарда-Джонса:

    Потенциал Леннарда-Джонса: U(r) = 4ε[(σ/r)¹² - (σ/r)⁶]
    Отсюда сила: F(r) = -dU/dr = 24ε[2(σ/r)¹³ - (σ/r)⁷] * (r_vector/r)

    ε (epsilon) - глубина потенциальной ямы (сила притяжения)
    σ (sigma) - расстояние, где потенциал = 0 (размер частицы)
    """
    N = len(positions)
    dr_vec = positions.reshape((N, 1, 3)) - positions.reshape((1, N, 3))

    r_sq = (dr_vec ** 2).sum(axis=2)
    np.fill_diagonal(r_sq, np.inf)  # Исключаем сам с собой
    mask = r_sq < r_cutoff_sq  # Учитываем только близкие частицы

    forces = np.zeros_like(positions)
    potential_energy = 0.0

    for i in range(N):
        for j in range(i + 1, N):
            if mask[i, j]:
                type_i = particle_types[i]
                type_j = particle_types[j]

                epsilon = epsilon_matrix[type_i, type_j]  # Сила взаимодействия
                sigma = sigma_matrix[type_i, type_j]  # Размер взаимодействия

                r = np.sqrt(r_sq[i, j])
                r_inv = 1.0 / r
                sigma_r = sigma * r_inv
                sigma_r6 = sigma_r ** 6
                sigma_r12 = sigma_r6 ** 2

                # СИЛА по производной потенциала:
                force_mag = 24.0 * epsilon * (2.0 * sigma_r12 - sigma_r6) * r_inv
                force_vec = force_mag * (positions[i] - positions[j]) * r_inv

                forces[i] += force_vec
                forces[j] -= force_vec  # 3-й закон Ньютона

                # ПОТЕНЦИАЛЬНАЯ ЭНЕРГИЯ (то, что в формуле Леннарда-Джонса):
                potential_energy += 4.0 * epsilon * (sigma_r12 - sigma_r6)

    return forces, potential_energy


# --- 2. THERMOSTAT AND PHASE CONTROL ---

def berendsen_thermostat(velocities, T_desired, T_current, tau=0.1):
    """Термостат Берендсена - поддерживает нужную температуру"""
    if T_current > 0:
        scale = np.sqrt(1 + (dt / tau) * (T_desired / T_current - 1))
        velocities *= scale
    return velocities


def calculate_pressure(positions, velocities, masses, L, r_cutoff_sq, particle_types, epsilon_matrix, sigma_matrix):
    """
    Расчет давления по вириальной теореме:
    P = (N*kT + W)/V, где:
    - N*kT = кинетическая часть (идеальный газ)
    - W = вириал = сумма(r_ij * F_ij) / 2
    - V = объем куба
    """
    N = len(positions)
    volume = L ** 3

    forces, _ = calculate_forces_multi(positions, L, r_cutoff_sq, particle_types, epsilon_matrix, sigma_matrix)
    virial = np.sum(forces * positions)  # Вириальная часть

    # Кинетическая энергия с учетом масс:
    kinetic_energy = 0.5 * np.sum(masses * np.sum(velocities ** 2, axis=1))
    T_current = 2.0 * kinetic_energy / (3 * N)  # Температура из кинетической теории

    pressure = (N * T_current + virial / 3) / volume
    return pressure


# --- 3. PHASE TRANSITION DETECTION ---

def analyze_phase(positions, L, cluster_threshold=1.5):
    """
    Анализ фазового состояния через поиск кластеров:
    - Если есть один большой кластер (>70% частиц) - ЖИДКОСТЬ
    - Если несколько средних кластеров - ДВУХФАЗНАЯ ОБЛАСТЬ
    - Если много маленьких кластеров - ГАЗ
    """
    N = len(positions)
    clusters = []
    visited = set()

    for i in range(N):
        if i not in visited:
            cluster = [i]
            queue = [i]
            visited.add(i)

            while queue:
                current = queue.pop(0)
                for j in range(N):
                    if j not in visited:
                        r_sq = np.sum((positions[current] - positions[j]) ** 2)
                        if r_sq < cluster_threshold ** 2:
                            cluster.append(j)
                            queue.append(j)
                            visited.add(j)

            clusters.append(cluster)

    cluster_sizes = [len(cluster) for cluster in clusters]
    max_cluster_size = max(cluster_sizes) if cluster_sizes else 0
    avg_cluster_size = np.mean(cluster_sizes) if cluster_sizes else 0

    # Определение фазы:
    if max_cluster_size > N * 0.7:  # Большой кластер = жидкость
        phase = "LIQUID"
    elif max_cluster_size > N * 0.3:  # Средние кластеры = двухфазная область
        phase = "TWO-PHASE"
    else:  # Маленькие кластеры = газ
        phase = "GAS"

    return phase, clusters, max_cluster_size, avg_cluster_size


# --- 4. STYLE & VISUALIZATION FUNCTIONS ---

def get_particle_color(particle_type, phase):
    """Цвета частиц по типам и фазам"""
    colors = [
        color.red,  # Тип 0 - тяжелые частицы
        color.blue,  # Тип 1 - легкие частицы
        color.green,  # Тип 2 (запас)
        color.yellow,  # Тип 3 (запас)
    ]

    if phase == "LIQUID":
        return colors[particle_type % len(colors)]
    elif phase == "TWO-PHASE":
        return color.orange
    else:  # GAS
        return color.gray(0.7)


def get_particle_radius(mass, base_mass=1.0):
    """Радиус частицы пропорционален кубическому корню из массы"""
    return 0.08 * (mass / base_mass) ** (1 / 3)


def update_particle_appearance(particles, positions, particle_types, masses, current_phase, clusters):
    """Обновление внешнего вида частиц в зависимости от фазы и массы"""
    N = len(particles)
    max_cluster = max(clusters, key=len) if clusters else []

    for i in range(N):
        particle_type = particle_types[i]
        mass = masses[i]
        color = get_particle_color(particle_type, current_phase)
        radius = get_particle_radius(mass)

        # Настройки по фазам:
        if current_phase == "LIQUID":
            opacity = 0.9
            radius *= 1.2  # В жидкости частицы кажутся ближе
        elif current_phase == "TWO-PHASE":
            opacity = 0.7
        else:  # GAS
            opacity = 0.5
            radius *= 0.9  # В газе дальше друг от друга

        particles[i].color = color
        particles[i].opacity = opacity
        particles[i].radius = radius

        # Подсветка границ кластеров
        if i in max_cluster and current_phase == "TWO-PHASE":
            particles[i].emissive = True
        else:
            particles[i].emissive = False


def update_style_links(particles, positions, link_radius, link_cutoff_sq, current_phase):
    """Обновление связей между частицами"""
    global links
    for link in links:
        link.visible = False
    links = []

    N = len(positions)
    for i in range(N):
        for j in range(i + 1, N):
            dr_vec = positions[i] - positions[j]
            r_sq = (dr_vec ** 2).sum()
            if r_sq < link_cutoff_sq:
                if current_phase == "LIQUID":
                    link_color = color.red
                    opacity = 0.6
                elif current_phase == "TWO-PHASE":
                    link_color = color.orange
                    opacity = 0.4
                else:
                    link_color = color.blue
                    opacity = 0.2

                pos_i = vec(positions[i][0], positions[i][1], positions[i][2])
                pos_j = vec(positions[j][0], positions[j][1], positions[j][2])
                link = cylinder(pos=pos_i, axis=(pos_j - pos_i),
                                radius=link_radius, color=link_color, opacity=opacity)
                links.append(link)


# --- 5. INTERACTIVE CONTROLS ---

def create_controls():
    """Создание элементов управления интерфейсом"""
    scene.append_to_caption('\n\n')
    scene.append_to_caption('<b>🎮 ИНТЕРАКТИВНОЕ УПРАВЛЕНИЕ:</b>\n\n')

    button(text='⏸️ Пауза', bind=toggle_pause)
    button(text='🔄 Сброс', bind=reset_simulation)
    button(text='❄️ Охладить', bind=cool_system)
    button(text='🔥 Нагреть', bind=heat_system)
    button(text='💧 Сжать', bind=compress_system)

    scene.append_to_caption('\n\n')

    scene.append_to_caption('<b>Температура:</b> ')
    temp_slider = slider(min=0.1, max=5.0, value=T, step=0.1, bind=set_temperature)

    scene.append_to_caption('<b>Размер ящика:</b> ')
    size_slider = slider(min=5, max=25, value=L, step=1, bind=set_box_size)

    scene.append_to_caption('<b>Доля тяжелых:</b> ')
    ratio_slider = slider(min=0.0, max=1.0, value=0.5, step=0.1, bind=set_particle_ratio)


def toggle_pause():
    global paused
    paused = not paused


def reset_simulation():
    global positions, velocities, accelerations, step, particle_types, masses
    particle_types = initialize_particle_types(N, particle_ratio)
    positions, velocities, masses = initialize_system(N, L, T, particle_types, mass_types)
    accelerations = np.zeros_like(positions)
    step = 0


def cool_system():
    global T
    T = max(0.1, T * 0.7)


def heat_system():
    global T
    T = min(5.0, T * 1.3)


def compress_system():
    global L
    L = max(5, L * 0.8)


def set_temperature(s):
    global T
    T = s.value


def set_box_size(s):
    global L
    L = s.value


def set_particle_ratio(s):
    global particle_ratio, particle_types, masses
    particle_ratio = s.value
    particle_types = initialize_particle_types(N, particle_ratio)
    masses = np.array([mass_types[t] for t in particle_types])


def initialize_particle_types(N, ratio):
    """Инициализация типов частиц: 0 = тяжелые, 1 = легкие"""
    types = []
    for i in range(N):
        if random.random() < ratio:
            types.append(0)  # Тяжелые частицы
        else:
            types.append(1)  # Легкие частицы
    return types


# --- 3. SIMULATION PARAMETERS ---
# -------------------------------------------------------------------
# ОСНОВНЫЕ ПАРАМЕТРЫ СИМУЛЯЦИИ:
# -------------------------------------------------------------------

N = 60  # Количество частиц в системе
L = 15.0  # Размер кубической ячейки (сторона куба)
T = 10.0  # Начальная температура системы
dt = 0.0005  # Шаг времени для интегрирования (меньше = точнее, но медленнее)

# ПАРАМЕТРЫ ВЗАИМОДЕЙСТВИЯ:
r_cutoff = 3.0  # Максимальное расстояние для расчета сил
r_cutoff_sq = r_cutoff ** 2  # Квадрат расстояния (для оптимизации)

# ВИЗУАЛИЗАЦИЯ:
link_radius = 0.03  # Толщина линий-связей между частицами
link_cutoff = 1.5  # Расстояние для показа связей
link_cutoff_sq = link_cutoff ** 2

# СОСТАВ СИСТЕМЫ:
particle_ratio = 0.5  # Доля тяжелых частиц (0.5 = половина тяжелых, половина легких)

# МАССЫ ЧАСТИЦ (теперь есть!):
mass_types = {
    0: 4.0,  # Тяжелые частицы (масса = 4)
    1: 1.0  # Легкие частицы (масса = 1)
}

# ПАРАМЕТРЫ ЛЕННАРДА-ДЖОНСА для разных комбинаций частиц:
# epsilon - сила взаимодействия (глубина потенциальной ямы)
# sigma - характерный размер взаимодействия

epsilon_matrix = np.array([
    # Тяжелые-Тяжелые    Тяжелые-Легкие
    [1.0, 0.7],  # [A-A, A-B]
    # Легкие-Тяжелые    Легкие-Легкие
    [0.7, 0.5]  # [B-A, B-B]
])

sigma_matrix = np.array([
    # Тяжелые-Тяжелые    Тяжелые-Легкие
    [1.2, 1.0],  # [A-A, A-B]
    # Легкие-Тяжелые    Легкие-Легкие
    [1.0, 0.8]  # [B-A, B-B]
])

# ТЕХНИЧЕСКИЕ ПАРАМЕТРЫ:
links = []  # Список графических связей
update_log_step = 10  # Как часто обновлять графики и логи
update_hist_step = 100  # Как часто обновлять гистограмму
n_bins = 20  # Количество столбцов в гистограмме
log_len = 15  # Длина лога в интерфейсе
paused = False  # Флаг паузы

RUN_ID = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
CSV_FILENAME = f"md_mass_phase_log_{RUN_ID}.csv"

# --- 7. SYSTEM INITIALIZATION ---
particle_types = initialize_particle_types(N, particle_ratio)
positions, velocities, masses = initialize_system(N, L, T, particle_types, mass_types)
accelerations = np.zeros_like(positions)

# --- 8. VPYTHON SETUP ---
scene = canvas(title='<b>MD SIMULATOR: MASS + PHASE TRANSITIONS</b>',
               width=900, height=400,
               center=vec(0, 0, 0), background=color.black)

# Стенки ящика
box_walls = box(pos=vec(0, 0, 0), size=vec(L, L, L), opacity=0.15, color=color.white)

# Создаем частицы с разными размерами по массе
particles = []
for i in range(N):
    p = positions[i]
    mass = masses[i]
    particle_color = get_particle_color(particle_types[i], "GAS")
    radius = get_particle_radius(mass)
    particle = sphere(pos=vec(p[0], p[1], p[2]),
                      radius=radius, color=particle_color, opacity=0.7)
    particles.append(particle)

# --- Графики ---
scene.append_to_caption('\n\n')
energy_graph = graph(width=900, height=200, title='<b>Energy and Phase Transitions</b>',
                     xtitle='Step', ytitle='Energy (E)')
ek_curve = gcurve(graph=energy_graph, color=color.orange, label='Kinetic (Ek)')
ep_curve = gcurve(graph=energy_graph, color=color.blue, label='Potential (Ep)')
et_curve = gcurve(graph=energy_graph, color=color.black, label='Total (Et)', width=2)

scene.append_to_caption('\n')
histogram_graph = graph(width=450, height=200, title='<b>Speed Distribution</b>',
                        xtitle='Speed (v)', ytitle='Count')
speed_histogram = gvbars(graph=histogram_graph, delta=0.1, color=color.red)

phase_graph = graph(width=450, height=200, title='<b>Phase Analysis</b>',
                    xtitle='Step', ytitle='Cluster Size')
cluster_curve = gcurve(graph=phase_graph, color=color.purple, label='Max Cluster')

# --- 9. TERMINAL AND LOGGING SETUP ---
static_info = [
    "<b>--- 🔬 SYSTEM WITH MASSES ---</b>",
    f" RUN ID:     {RUN_ID}",
    " MODEL:      Multi-type with Mass",
    " MASSES:     Heavy(4.0) + Light(1.0)",
    f" N (total):  {N}", f" L (box):    {L}",
    f" T (init):   {T}", f" Heavy/Light: {particle_ratio:.1f}",
    "<b>--- PHYSICS EXPLANATION ---</b>",
    "  Kinetic E = Σ(½ m v²)  - зависит от массы!",
    "  Potential E = Σ U(LJ)  - энергия взаимодействия",
    "  Pressure = (NkT + W)/V - вириальная теорема",
    "", "<b>--- 📈 REAL-TIME LOG ---</b>"
]

energy_log = deque(maxlen=log_len)
for _ in range(log_len): energy_log.appendleft("")

print(f"Logging data to file: {CSV_FILENAME}")
csv_file = open(CSV_FILENAME, 'w', newline='', encoding='utf-8')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(["Step", "Time_s", "Kinetic_Energy", "Potential_Energy", "Total_Energy",
                     "Temperature", "Pressure", "Phase", "Max_Cluster_Size", "Avg_Cluster_Size"])
csv_file.flush()

# Создаем элементы управления
create_controls()

# --- 10. MAIN SIMULATION LOOP ---
step = 0
current_phase = "GAS"
print("Simulation running with MASSES! Use controls to manipulate phase transitions!")

while True:
    if not paused:
        rate(100)

        # --- 1. ИНТЕГРИРОВАНИЕ (Верле) с учетом масс ---
        velocities = velocities + 0.5 * accelerations * dt

        # Движение не зависит от массы (v = v + a*dt)
        positions = positions + velocities * dt

        # --- 2. Граничные условия: отскок от стенок ---
        hit_upper = positions > (L / 2)
        positions[hit_upper] = L / 2
        velocities[hit_upper] *= -1

        hit_lower = positions < (-L / 2)
        positions[hit_lower] = -L / 2
        velocities[hit_lower] *= -1

        # --- 3. Расчет сил (без масс) ---
        forces, potential_energy = calculate_forces_multi(positions, L, r_cutoff_sq,
                                                          particle_types, epsilon_matrix, sigma_matrix)

        # УСКОРЕНИЕ = СИЛА / МАССА (вот где масса важна!)
        accelerations = forces / masses[:, np.newaxis]

        # --- 4. Завершаем шаг Верле ---
        velocities = velocities + 0.5 * accelerations * dt

        # --- 5. Контроль температуры (учитываем массы!) ---
        # Кинетическая энергия теперь зависит от масс:
        kinetic_energy = 0.5 * np.sum(masses * np.sum(velocities ** 2, axis=1))
        T_current = 2.0 * kinetic_energy / (3 * N)  # Температура из кинетической теории

        velocities = berendsen_thermostat(velocities, T, T_current)

        # --- 6. Анализ фазового состояния ---
        if step % 50 == 0:
            current_phase, clusters, max_cluster_size, avg_cluster_size = analyze_phase(positions, L)

        # --- 7. Визуальное обновление ---
        for i in range(N):
            p = positions[i]
            particles[i].pos = vec(p[0], p[1], p[2])

        if step % 5 == 0:
            update_particle_appearance(particles, positions, particle_types, masses, current_phase, clusters)
            update_style_links(particles, positions, link_radius, link_cutoff_sq, current_phase)

        # --- 8. Логирование и графики ---
        if step % update_log_step == 0:
            total_energy = kinetic_energy + potential_energy
            sim_time_s = step * dt

            # Расчет давления с учетом масс
            pressure = calculate_pressure(positions, velocities, masses, L, r_cutoff_sq,
                                          particle_types, epsilon_matrix, sigma_matrix)

            if not np.isnan(total_energy):
                # Графики энергий
                ek_curve.plot(step, kinetic_energy)
                ep_curve.plot(step, potential_energy)
                et_curve.plot(step, total_energy)
                cluster_curve.plot(step, max_cluster_size)

                # Логирование
                log_entry = (f"<b>STEP {step:<6}</b> | "
                             f"Et: {total_energy:7.2f} | "
                             f"Ek: {kinetic_energy:6.2f} | "
                             f"Ep: {potential_energy:6.2f} | "
                             f"Phase: {current_phase}")
                energy_log.appendleft(log_entry)

                # Запись в CSV
                csv_writer.writerow([step, sim_time_s, kinetic_energy, potential_energy, total_energy,
                                     T_current, pressure, current_phase, max_cluster_size, avg_cluster_size])
                csv_file.flush()

            # Обновление интерфейса
            caption_text = "<pre>"
            for i in range(log_len):
                static_line = static_info[i] if i < len(static_info) else ""
                log_line = energy_log[i] if i < len(energy_log) else ""
                caption_text += f"{static_line:<55} | {log_line:<60}\n"
            caption_text += f"\n<b>Current: T={T_current:.2f}, P={pressure:.2f}, Phase={current_phase}, Max Cluster={max_cluster_size}</b>"
            caption_text += "</pre>"
            scene.caption = caption_text

        # Гистограмма скоростей
        if step % update_hist_step == 0 and not np.isnan(total_energy):
            speeds = np.linalg.norm(velocities, axis=1)
            v_max = np.max(speeds) * 1.1
            hist_counts, bin_edges = np.histogram(speeds, bins=n_bins, range=(0, v_max))
            vpython_hist_data = []
            bin_width = bin_edges[1] - bin_edges[0]
            for i in range(n_bins):
                vpython_hist_data.append([bin_edges[i] + bin_width / 2.0, hist_counts[i]])
            speed_histogram.data = vpython_hist_data

    step += 1