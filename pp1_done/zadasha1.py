def calculate_formula(n, r, pi=3.141592653589793, precision=10):
    """
    Обчислює формулу: ((2r)^n * (π/2)^[n/2]) / n!!
    Параметри:
    n - натуральне число int
    r - дійсне число float
    pi - значення π 3.141592653589793
    precision - точність округлення після точки ##.(#######)
    """
    def double_factorial(x):
        """Локальна функція для обчислення подвійного факторіалу"""
        result = 1
        while x > 0:
            result *= x # подвійний факторіал (добуток чисел з кроком 2) (5*3*1=15)
            x -= 2
        return result
    # Компоненти формули
    power_2r = (2 * r) ** n        # (2r)^n
    power_pi = (pi / 2) ** (n // 2) # (π/2)^[n/2], де n//2 — ціла частина
    dfactorial = double_factorial(n) # n!!

    result = (power_2r * power_pi) / dfactorial
    return round(result, precision) #  round округлює число до потрібної кількості знаків після коми
# --------
n_val = 5
r_val = 10
result = calculate_formula(n_val, r_val)
print(f"Результат n={n_val}, r={r_val} : {result}")
