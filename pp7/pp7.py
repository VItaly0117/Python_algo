import matplotlib.pyplot as plt
import csv
import os
# --- 1. Налаштування ---
file_csv = 'function_data_python.csv'
# --- 2. Підготовка даних ---
x_values = []
y_values = []
# --- 3. Читання файлу ---
try:
    with open(file_csv, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter=',')

        try:
            header = next(reader)
            print(f"Читаємо файл '{file_csv}'. Пропущено заголовок: {header}")
            for row in reader:
                x_values.append(float(row[0]))  # row[0] - це перший стовпець (X)
                y_values.append(float(row[1]))  # row[1] - це другий стовпець (Y)

        except StopIteration:
            print(f"Помилка: Файл '{file_csv}' порожній.")
            exit()
        except (ValueError, IndexError) as e:
            print(f"Помилка: Неправильний формат даних у файлі '{file_csv}'.")
            print(f"Перевірте рядок, де сталася помилка (можливо, після нього): {row}")
            exit()
    print(f"Дані з CSV успішно завантажені. Всього точок: {len(x_values)}")

    # --- 4. Побудова графіка (Matplotlib) ---
    plt.figure(figsize=(10, 6))
    plt.plot(x_values, y_values,
             color='blue',
             linestyle='-',
             label='y = x * sin(x)')
    # --- 5. Налаштування вигляду графіка ---
    plt.title('Графік функції')  # Назва графіка
    plt.xlabel('Вісь X')  # Підпис осі X
    plt.ylabel('Вісь Y')  # Підпис осі Y
    plt.legend()  # Показати легенду (мітку 'label' з plt.plot)
    plt.grid(True)  # Увімкнути сітку
    # Додаємо чіткі лінії для осей X та Y (на рівні 0)
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    # Зберігаємо графік у файл (картинку .png) у ту саму папку
    plot_file = 'function_plot_from_csv.png'
    plt.savefig(plot_file)
    print(f"Графік збережено у файл: {plot_file}")
    plt.show()
# --- 6. Обробка помилок ---
except FileNotFoundError:
    print(f"--- ПОМИЛКА ---")
    print(f"Файл '{file_csv}' не знайдено!")
    print(f"Переконайся, що 'pp7.py' та '{file_csv}' лежать в одній папці.")
except Exception as e:
    # "Ловимо" будь-які інші непередбачені помилки
    print(f"Сталася невідома помилка: {e}")