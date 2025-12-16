import sys
import task_1_1
import task_1_2
import task_1_3
import task_2


def print_menu():
    print("\n" + "=" * 40)
    print(" ЛАБОРАТОРНА РОБОТА №1 (ГОЛОВНЕ МЕНЮ)")
    print("=" * 40)
    print("1. Завдання 1.1: Дослід Міллікена (Статистика + Гістограма)")
    print("2. Завдання 1.2: Напруга в мережі (Довірчі інтервали)")
    print("3. Завдання 1.3: Кореляція (Температура vs Міцність)")
    print("4. Завдання 2: Сімейство кривих Гауса")
    print("0. Вихід")
    print("-" * 40)


def main():
    while True:
        print_menu()
        choice = input("Введіть номер завдання > ")

        if choice == '1':
            task_1_1.run_task()
        elif choice == '2':
            task_1_2.run_task()
        elif choice == '3':
            task_1_3.run_task()
        elif choice == '4':
            task_2.run_task()
        elif choice == '0':
            print("Вихід з програми.")
            break
        else:
            print("Помилка: Невірне введення, спробуйте ще раз.")

        input("\nНатисніть Enter, щоб повернутися в меню...")


if __name__ == "__main__":
    main()