#задача в тг скрин есть
from math import exp
def calculate_Z(x, a, b, c):
    if x == 125:
        return b + a * exp(x)
    elif x == 200:
        return c - b + x
    elif 0 < x < 125:
        return exp(x) + a
    else:
        return 10
def calculate_Q(Z, a, b, c):
    return (a / Z) + (b / (2 * Z)) - c
def calculate_A(Q):
    if Q > 0:
        return Q + 3
    else:
        return Q - 4
# -------
def main(x=10, a=2, b=3, c=4):
    Z = calculate_Z(x, a, b, c)
    Q = calculate_Q(Z, a, b, c)
    A = calculate_A(Q)

    print(f"x={x}, a={a}, b={b}, c={c}")
    print(f"Z = {Z}")
    print(f"Q = {Q}")
    print(f"A = {A}")
main()
#а з обробкою виключень
# задача в тг скрин есть
from math import exp


def calculate_Z(x, a, b, c):
    if x == 125:
        return b + a * exp(x)
    elif x == 200:
        return c - b + x
    elif 0 < x < 125:
        return exp(x) + a
    else:
        return 10


def calculate_Q(Z, a, b, c):
    """Обчислення Q з обробкою ділення на нуль."""
    try:
        return (a / Z) + (b / (2 * Z)) - c
    except ZeroDivisionError:
        print(f"Помилка: Ділення на нуль при обчисленні Q (Z = {Z}).")
        return None  # Повертаємо None як сигнал помилки


def calculate_A(Q):
    if Q is None:  # Перевірка, якщо Q не вдалося обчислити
        return None

    if Q > 0:
        return Q + 3
    else:
        return Q - 4


# -------
def main(x=10, a=2, b=3, c=4):
    Z = calculate_Z(x, a, b, c)
    Q = calculate_Q(Z, a, b, c)

    # Якщо Q не обчислено через помилку, A теж не можна рахувати
    if Q is None:
        A = None
        print("Не вдалося обчислити Q та A через математичну помилку.")
    else:
        A = calculate_A(Q)

    print(f"x={x}, a={a}, b={b}, c={c}")
    print(f"Z = {Z}")
    print(f"Q = {Q}")
    print(f"A = {A}")


main()