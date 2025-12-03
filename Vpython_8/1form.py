from vpython import *

# Настройка сцены (окна визуализации)
scene.width = 800
scene.height = 600
scene.title = "Пример 1: Сфера с текстурой\n"

# --- УПРАВЛЕНИЕ КАМЕРОЙ ---
# (Включено по умолчанию, но добавляем для ясности)
scene.userspin = True   # Разрешить вращение (правая кнопка мыши)
scene.userpan = True    # Разрешить перемещение (Shift + левая кнопка)
scene.userzoom = True   # Разрешить зум (колесо мыши)
# -------------------------

# Создаем сферу с текстурой Земли
earth = sphere(pos=vector(0, 0, 0),
               radius=1,
               texture=textures.earth)

# Добавим полупрозрачную "атмосферу" вокруг
atmosphere = sphere(pos=vector(0, 0, 0),
                    radius=1.05,
                    color=color.cyan,
                    opacity=0.3)

# Добавим источник света
scene.lights = [distant_light(direction=vector(1, 0.5, 0.5), color=color.white)]