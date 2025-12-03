from vpython import *

# --- НАСТРОЙКИ ---
scene.width = 1000
scene.height = 800
scene.title = "Chess: Clean & Simple"
scene.background = color.gray(0.1)  # Темный фон, чтобы глаза не резало
scene.center = vector(0, 0, 0)  # Камера смотрит в центр
scene.camera.pos = vector(0, 10, 15)  # Удобный угол обзора

# --- РАЗМЕРЫ ---
SQ_SIZE = 2.0  # Размер клетки
BOARD_H = 0.5  # Толщина доски


# Поверхность доски будет на высоте Y = 0.
# Сама доска (box) рисуется центром в -BOARD_H/2, чтобы верхняя грань была в 0.

# --- ФУНКЦИИ ГЕНЕРАЦИИ (возвращают объект) ---

def create_piece(type_char, x, z, color_team):
    # type_char: P, R, N, B, Q, K

    # Определяем высоту и форму
    if type_char == 'P':  # Пешка
        h = 1.5
        # Пешка состоит из цилиндра и шара.
        # Чтобы не париться с compound и смещением центров,
        # просто рисуем их относительно базовой точки.
        parts = [
            cylinder(pos=vector(x, 0, z), axis=vector(0, h * 0.8, 0), radius=SQ_SIZE * 0.3, color=color_team),
            sphere(pos=vector(x, h * 0.8, z), radius=SQ_SIZE * 0.25, color=color_team)
        ]
        return parts

    elif type_char == 'R':  # Ладья
        h = 2.0
        parts = [
            cylinder(pos=vector(x, 0, z), axis=vector(0, h, 0), radius=SQ_SIZE * 0.35, color=color_team),
            # Зубцы сверху
            cylinder(pos=vector(x, h, z), axis=vector(0, 0.2, 0), radius=SQ_SIZE * 0.4, color=color_team)
        ]
        return parts

    elif type_char == 'N':  # Конь
        h = 2.0
        parts = [
            cylinder(pos=vector(x, 0, z), axis=vector(0, h * 0.4, 0), radius=SQ_SIZE * 0.35, color=color_team),
            # Тело (коробка)
            box(pos=vector(x, h * 0.7, z), size=vector(SQ_SIZE * 0.4, h * 0.6, SQ_SIZE * 0.4), color=color_team),
            # Морда (смотрит вперед или назад) - просто блок сверху
            box(pos=vector(x, h, z + 0.2), size=vector(SQ_SIZE * 0.3, SQ_SIZE * 0.4, SQ_SIZE * 0.6), color=color_team)
        ]
        return parts

    elif type_char == 'B':  # Слон
        h = 2.3
        parts = [
            cylinder(pos=vector(x, 0, z), axis=vector(0, h * 0.8, 0), radius=SQ_SIZE * 0.3, color=color_team),
            sphere(pos=vector(x, h * 0.8, z), radius=SQ_SIZE * 0.25, color=color_team),
            sphere(pos=vector(x, h, z), radius=SQ_SIZE * 0.1, color=color_team)  # Пипка
        ]
        return parts

    elif type_char == 'Q':  # Королева
        h = 2.6
        parts = [
            cylinder(pos=vector(x, 0, z), axis=vector(0, h * 0.9, 0), radius=SQ_SIZE * 0.35, color=color_team),
            sphere(pos=vector(x, h * 0.9, z), radius=SQ_SIZE * 0.35, color=color_team)
        ]
        return parts

    elif type_char == 'K':  # Король
        h = 2.8
        parts = [
            cylinder(pos=vector(x, 0, z), axis=vector(0, h * 0.9, 0), radius=SQ_SIZE * 0.35, color=color_team),
            box(pos=vector(x, h, z), size=vector(0.2, 0.6, 0.2), color=color_team),  # Крест верт
            box(pos=vector(x, h, z), size=vector(0.5, 0.2, 0.2), color=color_team)  # Крест гориз
        ]
        return parts


# --- СОЗДАНИЕ ДОСКИ ---
# Центрируем доску (сдвиг offset)
offset = 3.5 * SQ_SIZE

# Рисуем клетки
for row in range(8):
    for col in range(8):
        # Координаты X и Z
        x_pos = col * SQ_SIZE - offset
        z_pos = row * SQ_SIZE - offset

        # Цвет клетки
        if (row + col) % 2 == 0:
            c = vector(0.8, 0.6, 0.4)  # Светлая
        else:
            c = vector(0.4, 0.2, 0.1)  # Темная

        # Рисуем бокс
        # pos.y = -BOARD_H/2, значит верхняя грань ровно на y=0
        box(pos=vector(x_pos, -BOARD_H / 2, z_pos),
            size=vector(SQ_SIZE, BOARD_H, SQ_SIZE),
            color=c)

# Рамка вокруг
box(pos=vector(0, -BOARD_H / 2 - 0.1, 0),
    size=vector(SQ_SIZE * 8.5, BOARD_H, SQ_SIZE * 8.5),
    color=vector(0.2, 0.1, 0.05))

# --- РАССТАНОВКА ФИГУР ---

# Схема (Белые внизу Z > 0 (условно), Черные вверху)
# Используем стандартный порядок
back_row = ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']

c_white = vector(1, 1, 0.9)
c_black = vector(0.2, 0.2, 0.2)

for i in range(8):
    x = i * SQ_SIZE - offset

    # --- БЕЛЫЕ ---
    # Пешки (Ряд 1 -> Z координата ближе к нам)
    # VPython Z axis: + на нас, - от нас.
    # Пусть белые будут на Z = row 0 (дальний край) или row 7?
    # Сделаем классику: Белые на row 0, 1. Черные на 6, 7.

    z_white_back = 0 * SQ_SIZE - offset
    z_white_pawn = 1 * SQ_SIZE - offset

    create_piece(back_row[i], x, z_white_back, c_white)
    create_piece('P', x, z_white_pawn, c_white)

    # --- ЧЕРНЫЕ ---
    z_black_pawn = 6 * SQ_SIZE - offset
    z_black_back = 7 * SQ_SIZE - offset

    create_piece(back_row[i], x, z_black_back, c_black)
    create_piece('P', x, z_black_pawn, c_black)

print("Готово. Фигуры стоят на доске.")