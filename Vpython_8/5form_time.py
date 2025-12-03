from vpython import *
from datetime import datetime

# Налаштування сцени
scene.width = 800
scene.height = 600
scene.title = "Пример 5: Анимированные часы\n"
scene.background = color.gray(0.3)

# --- УПРАВЛІННЯ КАМЕРОЮ ---
scene.userspin = True
scene.userpan = True
scene.userzoom = True
# -------------------------

# --- Статичні частини годинника ---

# Циферблат (плоский циліндр)
# Верхня грань циферблата знаходиться на Z = 0 (-0.1 + 0.1)
clock_face = cylinder(pos=vector(0, 0, -0.1),
                      axis=vector(0, 0, 0.1),
                      radius=5,
                      color=color.white)

# Обід
clock_rim = cylinder(pos=vector(0, 0, -0.15),
                     axis=vector(0, 0, 0.2),
                     radius=5.1,
                     color=color.gray(0.7))

# Центральна вісь
center_pin = cylinder(pos=vector(0, 0, 0),
                      axis=vector(0, 0, 0.2),
                      radius=0.1,
                      color=color.red)

# Створюємо 12 годинних міток
for i in range(12):
    angle = radians(i * 30)
    x = 4.5 * sin(angle)
    y = 4.5 * cos(angle)

    # ВИПРАВЛЕННЯ ТУТ:
    # Змінили Z з 0 на 0.06, щоб мітки були трохи вище поверхні циферблата
    tick = box(pos=vector(x, y, 0.06),
               size=vector(0.4, 0.4, 0.1),
               color=color.black)

# --- Динамічні частини (стрілки) ---

orig_s_axis = vector(0, 4.5, 0)
orig_m_axis = vector(0, 4.0, 0)
orig_h_axis = vector(0, 2.5, 0)

# Секундна стрілка (найвище, Z=0.1)
second_hand = arrow(pos=vector(0, 0, 0.1),
                    shaftwidth=0.05,
                    color=color.red,
                    axis=orig_s_axis)

# Хвилинна стрілка (посередині, Z=0.05)
minute_hand = arrow(pos=vector(0, 0, 0.05),
                    shaftwidth=0.15,
                    color=color.black,
                    axis=orig_m_axis)

# Годинна стрілка (найнижче, але над мітками, Z=0 -> підняли трохи стрілку теж для надійності)
hour_hand = arrow(pos=vector(0, 0, 0.02),
                  shaftwidth=0.25,
                  color=color.black,
                  axis=orig_h_axis)

# --- Анімаційний цикл ---
while True:
    rate(100)

    now = datetime.now()

    s = now.second + now.microsecond / 1000000
    m = now.minute + s / 60
    h = (now.hour % 12) + m / 60

    s_angle = -radians(s * 6)
    m_angle = -radians(m * 6)
    h_angle = -radians(h * 30)

    second_hand.axis = rotate(orig_s_axis, angle=s_angle, axis=vector(0, 0, 1))
    minute_hand.axis = rotate(orig_m_axis, angle=m_angle, axis=vector(0, 0, 1))
    hour_hand.axis = rotate(orig_h_axis, angle=h_angle, axis=vector(0, 0, 1))