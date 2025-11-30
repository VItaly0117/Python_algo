import custom_calculations as cc
def main_menu():
    while True:
        print("\n--- Головне Меню ---")
        print("1. Обчислити формулу з подвійним факторіалом (Задача 1)")
        print("2. Обчислити Z, Q, A (Задача 2)")
        print("3. Обчислити добуток P (Задача 3)")
        print("4. Порахувати непарні числа (Задача 4)")
        print("0. Вихід")

        choice = input("Оберіть опцію: ")

        if choice == '1':
            run_task1()
        elif choice == '2':
            run_task2()
        elif choice == '3':
            run_task3()
        elif choice == '4':
            run_task4()
        elif choice == '0':
            print("Завершення роботи.")
            break
        else:
            print("Невірний вибір, спробуйте ще раз.")

def run_task1():
    """Виконує демонстрацію функції calculate_formula."""
    print("\n--- Задача 1: Обчислення формули ---")
    try:
        n = int(input("Введіть натуральне число n: "))
        r = float(input("Введіть дійсне число r: "))
        result = cc.calculate_formula(n, r)
        print(f"Результат для n={n}, r={r} : {result}")
    except ValueError:
        print("Помилка: Будь ласка, введіть коректні числові дані.")


def run_task2():
    """Виконує демонстрацію функцій calculate_Z, Q, A."""
    print("\n--- Задача 2: Обчислення Z, Q, A ---")
    try:
        x = float(input("Введіть x (типово 10): ") or 10)
        a = float(input("Введіть a (типово 2): ") or 2)
        b = float(input("Введіть b (типово 3): ") or 3)
        c = float(input("Введіть c (типово 4): ") or 4)

        Z = cc.calculate_Z(x, a, b, c)
        Q = cc.calculate_Q(Z, a, b, c)
        A = cc.calculate_A(Q)

        print(f"\nДля x={x}, a={a}, b={b}, c={c}:")
        print(f"Z = {Z}")
        print(f"Q = {Q}")
        print(f"A = {A}")
    except ValueError:
        print("Помилка: Будь ласка, введіть коректні числові дані.")


def run_task3():
    """Виконує демонстрацію функції calculate_P."""
    print("\n--- Задача 3: Обчислення добутку P ---")
    try:
        n = int(input("Введіть натуральне число n: "))
        result = cc.calculate_P(n)
        if result is not None:
            print(f"Результат P = {result}")
    except ValueError:
        print("Помилка: Будь ласка, введіть ціле число.")


def run_task4():
    """Виконує демонстрацію функції count_odd_numbers."""
    print("\n--- Задача 4: Підрахунок непарних чисел ---")
    odd_count = cc.count_odd_numbers()
    print(f"\nКількість непарних чисел: {odd_count}")


if __name__ == "__main__":
    main_menu()