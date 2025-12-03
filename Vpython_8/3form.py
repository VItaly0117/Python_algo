from vpython import *

scene.width = 800
scene.height = 600
scene.title = "Пример 3: Составной объект (compound)\n"

# --- УПРАВЛЕНИЕ КАМЕРОЙ ---
scene.userspin = True   # Вращение (правая кнопка)
scene.userpan = True    # Перемещение (Shift + левая)
scene.userzoom = True   # Зум (колесо)
# -------------------------

# 1. Создаем "древко" стрелки
arrow_shaft = cylinder(pos=vector(0, 0, 0),
                       axis=vector(5, 0, 0),
                       radius=0.2,
                       color=color.yellow)

# 2. Создаем "наконечник"
arrow_head = cone(pos=vector(5, 0, 0),
                  axis=vector(1, 0, 0),
                  radius=0.4,
                  color=color.red)

# 3. Объединяем их в один объект
my_arrow = compound([arrow_shaft, arrow_head])

# Повернем всю стрелку на 45 градусов
my_arrow.rotate(angle=radians(45),
                axis=vector(0, 0, 1),
                origin=vector(0, 0, 0))