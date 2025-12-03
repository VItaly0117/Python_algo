from vpython import *
scene = canvas(title="Checkbox + Button", width=600, height=400)
scene.background = color.gray(0.9)
my_sphere = sphere(color=color.blue, radius=0.5)
my_sphere.visible = True
def on_check(c):
    wtext(text=f"Прапорець: {'вкл' if c.checked else 'викл'}\n")
def on_click(b):
    my_sphere.visible = not my_sphere.visible
checkbox(text="Виберіть мене", bind=on_check, checked=False)
wtext(text="\n")
button(text="Сховати / Показати кулю", bind=on_click)
scene.caption = "Примітив: checkbox - прапорець"
