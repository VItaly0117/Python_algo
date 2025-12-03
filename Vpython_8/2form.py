from vpython import *

scene.width = 800
scene.height = 600
scene.title = "Пример 2: Спираль (пружина)\n"
scene.background = color.gray(0.9)

# --- УПРАВЛЕНИЕ КАМЕРОЙ ---
scene.userspin = True   # Вращение (правая кнопка)
scene.userpan = True    # Перемещение (Shift + левая)
scene.userzoom = True   # Зум (колесо)
# -------------------------

# Создаем красную пружину
spring = helix(pos=vector(-5, 0, 0),
               axis=vector(10, 0, 0),
               radius=0.5,
               thickness=0.1,
               coils=20,
               color=color.red)

# Добавим шарики на концы
ball_start = sphere(pos=spring.pos, radius=0.2, color=color.blue)
ball_end = sphere(pos=spring.pos + spring.axis, radius=0.2, color=color.blue)