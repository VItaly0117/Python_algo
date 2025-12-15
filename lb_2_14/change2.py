#pp2
#
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
    dfactorial = double_factorial(n)

    # Стара перевірка через if
    if dfactorial == 0:
        print("Помилка: Подвійний факторіал від нуля не визначений у знаменнику.")
        return float('inf')

    result = (power_2r * power_pi) / dfactorial
    return round(result, precision)


#з обробкою виключень
def calculate_formula(n, r, pi=3.141592653589793, precision=10):
    """
    Обчислює формулу: ((2r)^n * (π/2)^[n/2]) / n!! з обробкою виключень.
    """

    def double_factorial(x):
        """Локальна функція для обчислення подвійного факторіалу."""
        result = 1
        for i in range(x, 0, -2):
            result *= i
        return result

    try:
        power_2r = (2 * r) ** n
        power_pi = (pi / 2) ** (n // 2)
        dfactorial = double_factorial(n)

        # Спроба виконати ділення. Якщо dfactorial == 0, Python викине ZeroDivisionError
        result = (power_2r * power_pi) / dfactorial

        return round(result, precision)

    except ZeroDivisionError:
        print("Помилка: Ділення на нуль (знаменник дорівнює 0).")
        return float('inf')

    except OverflowError:
        print("Помилка: Числа занадто великі для обчислення (OverflowError).")
        return float('inf')

    except TypeError:
        print("Помилка: Некоректний тип вхідних даних.")
        return None