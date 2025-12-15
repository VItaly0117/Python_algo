# -*- coding: utf-8 -*-
from math import cos, sin, exp

# --- Функції з zadasha1.py ---

def calculate_formula(n, r, pi=3.141592653589793, precision=10):
    """
    Обчислює формулу: ((2r)^n * (π/2)^[n/2]) / n!!

    Параметри:
    n (int): натуральне число
    r (float): дійсне число
    pi (float): значення π
    precision (int): точність округлення
    """

    def double_factorial(x):
        """Локальна функція для обчислення подвійного факторіалу."""
        result = 1
        for i in range(x, 0, -2):
            result *= i
        return result

    power_2r = (2 * r) ** n
    power_pi = (pi / 2) ** (n // 2)
    #
    dfactorial = double_factorial(n)


    if dfactorial == 0:
        print("Помилка: Подвійний факторіал від нуля не визначений у знаменнику.")
        return float('inf')

    result = (power_2r * power_pi) / dfactorial
    return round(result, precision)

# з обробкою виключень



# --- Функції з zadasha2.py ---

def calculate_Z(x, a, b, c):
    """Обчислює значення Z в залежності від x."""
    if x == 125:
        return b + a * exp(x)
    elif x == 200:
        return c - b + x
    elif 0 < x < 125:
        return exp(x) + a
    else:
        return 10


def calculate_Q(Z, a, b, c):
    """Обчислює значення Q."""
    if Z == 0:
        print("Помилка: Ділення на нуль при обчисленні Q.")
        return float('inf')
    return (a / Z) + (b / (2 * Z)) - c


def calculate_A(Q):
    """Обчислює значення A."""
    return Q + 3 if Q > 0 else Q - 4


# --- Функція з zadasha3.py ---

def calculate_P(n):
    """
    Обчислює добуток P = P_1 * P_2 * ... * P_n,
    де P_i = (cos(1)+...+cos(i)) / (sin(1)+...+sin(i)).
    """
    if not isinstance(n, int) or n <= 0:
        print("Помилка: n має бути натуральним числом.")
        return None

    product_P = 1.0
    sum_cos = 0.0
    sum_sin = 0.0

    for i in range(1, n + 1):
        sum_cos += cos(i)
        sum_sin += sin(i)

        if sum_sin == 0:
            print(f"Помилка: Ділення на нуль при i = {i}.")
            return float('inf')

        product_P *= sum_cos / sum_sin

    return product_P


# --- Функція з zadasha4.py ---

def count_odd_numbers():
    """
    Підраховує кількість непарних чисел, введених користувачем.
    """
    local_count = 0

    try:
        n = int(input("Введіть кількість чисел, які хочете перевірити: "))
        if n <= 0:
            print("Кількість чисел має бути додатною.")
            return 0
    except ValueError:
        print("Будь ласка, введіть ціле число.")
        return 0

    for i in range(1, n + 1):
        while True:
            try:
                a = int(input(f"Введіть число a_{i}: "))
                if a % 2 != 0:
                    local_count += 1
                break  # Вихід з циклу while, якщо введення коректне
            except ValueError:
                print("Ви ввели не ціле число. Спробуйте ще раз.")

    return local_count