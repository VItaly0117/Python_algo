from vpython import *
from datetime import datetime

# Настройка сцены
scene.width = 800
scene.height = 600
scene.title = "Пример 5: Анимированные часы\n"
scene.background = color.gray(0.3)

# --- УПРАВЛЕНИЕ КАМЕРОЙ ---
scene.userspin = True  # Вращение (правая кнопка)
scene.userpan = True  # Перемещение (Shift + левая)
scene.userzoom = True  # Зум (колесо)
# -------------------------

# --- Статические части часов ---

# Циферблат (плоский цилиндр)
clock_face = cylinder(pos=vector(0, 0, -0.1),
                      axis=vector(0, 0, 0.1),
                      radius=5,
                      color=color.white)

# Обод
clock_rim = cylinder(pos=vector(0, 0, -0.15),
                     axis=vector(0, 0, 0.2),
                     radius=5.1,
                     color=color.gray(0.7))

# Центральная ось
center_pin = cylinder(pos=vector(0, 0, 0),
                      axis=vector(0, 0, 0.2),
                      radius=0.1,
                      color=color.red)

# Создаем 12 часовых меток
for i in range(12):
    angle = radians(i * 30)  # 30 градусов на каждый час
    x = 4.5 * sin(angle)
    y = 4.5 * cos(angle)
    tick = box(pos=vector(x, y, 0),
               size=vector(0.4, 0.4, 0.1),  # Маленькие кубики-метки
               color=color.black)

# --- Динамические части (стрелки) ---
# Мы создаем их "стоя", указывая на 12 часов (по оси Y)
# Мы будем вращать их оси (axis) в цикле

# Исходные оси (положение на 12:00)
orig_s_axis = vector(0, 4.5, 0)
orig_m_axis = vector(0, 4.0, 0)
orig_h_axis = vector(0, 2.5, 0)

# Примитив arrow (стрелка) отлично подходит
second_hand = arrow(pos=vector(0, 0, 0.1),
                    shaftwidth=0.05,
                    color=color.red,
                    axis=orig_s_axis)

minute_hand = arrow(pos=vector(0, 0, 0.05),
                    shaftwidth=0.15,
                    color=color.black,
                    axis=orig_m_axis)

hour_hand = arrow(pos=vector(0, 0, 0),
                  shaftwidth=0.25,
                  color=color.black,
                  axis=orig_h_axis)

# --- Анимационный цикл ---
while True:
    rate(100)  # Ограничиваем цикл до 100 итераций в секунду

    # 1. Получаем текущее время
    now = datetime.now()

    # Добавляем доли, чтобы стрелки двигались плавно
    s = now.second + now.microsecond / 1000000
    m = now.minute + s / 60
    h = (now.hour % 12) + m / 60

    # 2. Рассчитываем углы
    # Умножаем на -1, чтобы вращать по часовой стрелке
    s_angle = -radians(s * 6)  # 360/60 = 6
    m_angle = -radians(m * 6)  # 360/60 = 6
    h_angle = -radians(h * 30)  # 360/12 = 30

    # 3. Обновляем оси стрелок
    # Мы каждый раз вращаем ОРИГИНАЛЬНУЮ ось
    # Это предотвращает накопление ошибок
    second_hand.axis = rotate(orig_s_axis, angle=s_angle, axis=vector(0, 0, 1))
    minute_hand.axis = rotate(orig_m_axis, angle=m_angle, axis=vector(0, 0, 1))
    hour_hand.axis = rotate(orig_h_axis, angle=h_angle, axis=vector(0, 0, 1))