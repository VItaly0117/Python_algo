from math import cos, sin
def calculate_P(n):
    """
    Обчислює добуток P = P_1 * P_2 * ... * P_n,
    де P_i = (cos(1)+...+cos(i)) / (sin(1)+...+sin(i)).
    Параметри:
    n - натуральне число int
    """
    if n <= 0:
        print("Помилка: n має бути натуральним числом.")
        return 0.0

    # Локальні змінні, що існують лише всередині функції
    local_P = 1.0
    sum_cos = 0.0
    sum_sin = 0.0

    for i in range(1, n + 1):
        sum_cos += cos(i)
        sum_sin += sin(i)

        # Перевірка на ділення на нуль
        if sum_sin == 0:
            print(f"Помилка: Ділення на нуль при i = {i}.")
            return float('inf')  # Повертаємо нескінченність

        local_P *= sum_cos / sum_sin

    return local_P

# --------
# Виклик функції з позиційним аргументом
n_val = int(input("Введіть n: "))
result_P = calculate_P(n_val)
print(f"Результат P = {result_P}")