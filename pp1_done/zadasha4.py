def count_odd_numbers(n):
    """
    Підраховує кількість непарних чисел, введених користувачем.
    Args:
        n (int): Кількість чисел, які потрібно ввести.
    Returns:
        int: Кількість непарних чисел.
    """
    local_count = 0  # Локальна змінна для підрахунку

    # Використовуємо цикл for, який є більш зручним для фіксованої кількості ітерацій
    for i in range(1, n + 1):
        try:
            a = int(input(f"Введіть число a_{i}: "))
            if a % 2 != 0:
                local_count += 1
        except ValueError:
            print("Ви ввели не ціле число.")
            # Щоб не "втратити" ітерацію, можна зменшити лічильник i
            i -= 1

    return local_count
try:
    num_to_enter = int(input("Кількість чисел n: "))
    # Виклик функції та збереження результату
    odd_count = count_odd_numbers(num_to_enter)
    print(f"Непарних чисел: {odd_count}")

except ValueError:
    print("Введіть ціле число")