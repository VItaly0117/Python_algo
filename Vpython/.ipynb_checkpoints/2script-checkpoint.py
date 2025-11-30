from vpython import *

# 1. Налаштування сцени
scene.width = 600
scene.height = 350
scene.title = "Додаток 1: Послідовна поява"
scene.background = color.gray(0.8)
scene.autoscale = False # Вимкнемо авто-масштаб, щоб камера не стрибала
scene.camera.pos = vector(0, 0.5, 10)

# 2. Створюємо "землю"
ground = box(pos=vector(0, -3, 0), size=vector(12, 0.2, 8), color=color.green)

# 3. Текстовий підпис для інформування
info_text = label(pos=vector(0, 4, 0),
                  text="Починаємо...",
                  height=20,
                  box=False,
                  background=color.gray(0.8))

# 4. Використовуємо rate() для паузи між додаванням об'єктів
# rate(N) означає "виконувати N ітерацій циклу в секунду".
# Якщо викликати її просто так, вона призупинить виконання на 1/N секунди.
# rate(1) = пауза ~1 секунда.

rate(1) # Пауза 1 сек

# 5. Додаємо box
info_text.text = "Додаємо: box (Паралелепіпед)"
my_box = box(pos=vector(-3, -1, 0), size=vector(2, 2, 2), color=color.red)

rate(1) # Пауза 1 сек

# 6. Додаємо sphere
info_text.text = "Додаємо: sphere (Сфера)"
my_sphere = sphere(pos=vector(0, -1, 0), radius=1, color=color.blue)

rate(1) # Пауза 1 сек

# 7. Додаємо cylinder
info_text.text = "Додаємо: cylinder (Циліндр)"
my_cylinder = cylinder(pos=vector(3, -2, 0), axis=vector(0, 2, 0), radius=0.8, color=color.yellow)

rate(1) # Пауза 1 сек

# 8. Додаємо arrow
info_text.text = "Додаємо: arrow (Стрілка)"
my_arrow = arrow(pos=vector(-4, 2, 0), axis=vector(8, 0, 0), color=color.orange, shaftwidth=0.3)

rate(1) # Пауза 1 сек

info_text.text = "Всі об'єкти завантажено!"