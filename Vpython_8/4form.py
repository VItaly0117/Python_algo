from vpython import *

scene.width = 800
scene.height = 600
scene.title = "Пример 4: Интерактивный виджет (slider)\n"

# --- УПРАВЛЕНИЕ КАМЕРОЙ ---
scene.userspin = True   # Вращение (правая кнопка)
scene.userpan = True    # Перемещение (Shift + левая)
scene.userzoom = True   # Зум (колесо)
# -------------------------

# Эта функция будет вызываться при движении слайдера
def change_radius(slider_widget):
    control_sphere.radius = slider_widget.value
    radius_text.text = f"Радиус: {slider_widget.value:.2f}"

# Создаем сферу, которой будем управлять
control_sphere = sphere(pos=vector(0, 2, 0), radius=1.0, color=color.green)

# Добавляем подпись к сцене (caption)
scene.append_to_caption("<h3>Управление радиусом сферы:</h3>\n")

# Создаем сам слайдер
radius_slider = slider(min=0.1,
                       max=3.0,
                       value=1.0,
                       step=0.1,
                       bind=change_radius)

# Добавляем текстовую метку
scene.append_to_caption("\n")
radius_text = wtext(text=f"Радиус: {control_sphere.radius:.2f}")