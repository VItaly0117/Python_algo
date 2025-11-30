from vpython import *

# 1. Налаштування сцени
scene.width = 600
scene.height = 400
scene.title = "Додаток 2: Всі основні форми"
scene.background = color.gray(0.9)
scene.camera.pos = vector(0, 1, 12)

# 2. Додаємо "землю" для кращої орієнтації
ground = box(pos=vector(0, -2.1, 0), size=vector(14, 0.2, 8), color=color.gray(0.5))

# --- Код для основних форм ---

# 3. box (Паралелепіпед)
b = box(pos=vector(-4, -1, 0),
        size=vector(2, 2, 2), # size - це зручна скорочення для length, height, width
        color=color.red)
label(pos=b.pos, text='box', yoffset=60, box=False, height=16)

# 4. sphere (Сфера)
s = sphere(pos=vector(0, -1, 0),
           radius=1,
           color=color.blue)
label(pos=s.pos, text='sphere', yoffset=60, box=False, height=16)

# 5. cylinder (Циліндр)
c = cylinder(pos=vector(4, -2, 0),
             axis=vector(0, 3, 0), # Вертикальний, висотою 3
             radius=0.8,
             color=color.yellow)
label(pos=vector(4, -0.5, 0), text='cylinder', yoffset=60, box=False, height=16)

# 6. arrow (Стрілка)
a = arrow(pos=vector(-5, 2, 0),
          axis=vector(10, 0, 0), # Горизонтальна, довжиною 10
          color=color.orange,
          shaftwidth=0.3)
label(pos=vector(0, 2, 0), text='arrow', yoffset=60, box=False, height=16)