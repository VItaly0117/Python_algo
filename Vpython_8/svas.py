from vpython import *

scene = canvas(width=600, height=400, background=color.white)
# Початковий ground: центр на -0.5, висота 1.0. Верхня поверхня на y=0.0
ground = box(pos=vector(0, -0.5, 0), size=vector(8, 1, 8), color=color.black)
# Початкова куля: радіус 0.5
ball = sphere(pos=vector(0, 3, 0), radius=0.5, color=color.magenta, make_trail=True)

# Початкова швидкість і гравітація
v = 0
g = 9.8
dt = 0.02

while True:
    rate(60)

    # 1. Оновлення швидкості
    v = v - g * dt

    # 2. Оновлення позиції
    ball.pos.y = ball.pos.y + v * dt

    # Відскок
    if ball.pos.y <= ball.radius:
        ball.pos.y = ball.radius
        v = -v * 0.9  # Втрата енергії при ударі