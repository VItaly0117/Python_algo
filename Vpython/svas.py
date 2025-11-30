from vpython import *

# --- Налаштування сцени ---
scene = canvas(title='Обертання L-подібного об\'єкта',
               width=800, height=600,
               background=color.gray(0.9),
               center=vector(0,0,0),
               range=8)

# Кольори українського прапора
blue_ukraine = vector(0, 0.337, 0.698)
yellow_ukraine = vector(1, 0.847, 0)

# --- Параметри об'єкта ---
center_radius = 0.5
arm_length = 3.0
arm_width = 0.8
arm_thickness = 0.2
secondary_arm_length = 3.0
secondary_arm_width = 0.8
secondary_arm_thickness = 0.2

# --- Створення частин об'єкта ---
parts = []

# Центральна частина
center_part = cylinder(pos=vector(0,0,-0.1),
                       axis=vector(0,0,0.2),
                       radius=center_radius,
                       color=blue_ukraine)
parts.append(center_part)

# --- Рука 1 (+X) та її додаток (+Y) ---
arm1 = box(pos=vector(arm_length/2, 0, 0),
           size=vector(arm_length, arm_width, arm_thickness),
           color=blue_ukraine)
parts.append(arm1)
sec_arm1 = box(pos=vector(arm_length, secondary_arm_length/2, 0),
               size=vector(secondary_arm_width, secondary_arm_length, secondary_arm_thickness),
               color=yellow_ukraine)
parts.append(sec_arm1)

# --- Рука 2 (-X) та її додаток (-Y) ---
arm2 = box(pos=vector(-arm_length/2, 0, 0),
           size=vector(arm_length, arm_width, arm_thickness),
           color=blue_ukraine)
parts.append(arm2)
sec_arm2 = box(pos=vector(-arm_length, -secondary_arm_length/2, 0),
               size=vector(secondary_arm_width, secondary_arm_length, secondary_arm_thickness),
               color=yellow_ukraine)
parts.append(sec_arm2)

# --- Рука 3 (+Y) та її додаток (-X) ---
arm3 = box(pos=vector(0, arm_length/2, 0),
           size=vector(arm_width, arm_length, arm_thickness),
           color=blue_ukraine)
parts.append(arm3)
sec_arm3 = box(pos=vector(-secondary_arm_length/2, arm_length, 0),
               size=vector(secondary_arm_length, secondary_arm_width, secondary_arm_thickness),
               color=yellow_ukraine)
parts.append(sec_arm3)

# --- Рука 4 (-Y) та її додаток (+X) ---
arm4 = box(pos=vector(0, -arm_length/2, 0),
           size=vector(arm_width, arm_length, arm_thickness),
           color=blue_ukraine)
parts.append(arm4)
sec_arm4 = box(pos=vector(secondary_arm_length/2, -arm_length, 0),
               size=vector(secondary_arm_length, secondary_arm_width, secondary_arm_thickness),
               color=yellow_ukraine)
parts.append(sec_arm4)

# --- Об'єднання в один об'єкт ---
complex_object = compound(parts)

# --- Анімація ---
rotation_axis = vector(0, 0, 1)
angular_velocity = 1.5
dt = 0.01

while True:
    rate(100)
    angle_step = angular_velocity * dt
    complex_object.rotate(angle=angle_step,
                         axis=rotation_axis,
                         origin=vector(0,0,0))