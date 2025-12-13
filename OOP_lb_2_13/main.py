from functions import compute, difference


def main():
    print("--- Лабораторна робота: Декоратори ---")
    print("Введіть 'q' для виходу.")

    while True:
        print("\n--- Новий розрахунок ---")
        user_input_x = input("Введіть число X: ")

        # Перевірка на вихід
        if user_input_x.lower() == 'q':
            break

        user_input_y = input("Введіть число Y: ")

        try:
            # КРОК 1: Конвертуємо введення користувача (рядок) у float
            # Ми робимо це тут, щоб передати у функцію саме число.
            # Якщо користувач ввів букви, програма впаде тут (ValueError),
            # і ми це зловимо в except.
            x = float(user_input_x)
            y = float(user_input_y)

            # КРОК 2: Викликаємо функцію
            # Тут спрацюють твої декоратори:
            # 1. validate перевірить, що це числа.
            # 2. convert перетворить їх на int (бо так сказано в завданні).
            # 3. clamp обріже результат, якщо він вийде за межі.
            result = compute(x, y)

            print(f"Результат compute({x}, {y}) = {result}")

        except ValueError:
            print("Помилка: Ви ввели не число! Спробуйте ще раз.")
        except TypeError as e:
            print(f"Помилка валідації (від декоратора): {e}")
        except Exception as e:
            print(f"Непередбачена помилка: {e}")


if __name__ == "__main__":
    main()