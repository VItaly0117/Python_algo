import pandas as pd
import matplotlib.pyplot as plt

# --- Налаштування файлів ---
file_from_python = 'coordinates_growing_wave.txt'
file_from_spreadsheet = 'function_data.csv'

try:
    # 1. Завантажуємо дані, згенеровані Python (роздільник - табуляція)
    data_py = pd.read_csv(file_from_python, sep='\t')
    print(data_py)
    # 2. Завантажуємо дані з Excel/Sheets (роздільник - кома)
    data_xls = pd.read_csv(file_from_spreadsheet,sep=';',decimal=",")
    print(data_xls)
    # 3. Створюємо графік
    plt.figure(figsize=(12, 7))  # Трохи ширший графік

    # 4. Малюємо дані з Python-файлу
    # 'b-' означає: 'b' - blue (синій), '-' - суцільна лінія
    # Маркери 'o' прибрані, бо точок дуже багато (200+) і вони зливаються
    plt.plot(data_py['x'], data_py['y'], 'b-', label='Дані з Python (TXT)')

    # 5. Малюємо дані з CSV-файлу
    # 'r--' означає: 'r' - red (червоний), '--' - пунктирна лінія
    # Робимо лінію трохи товщою, щоб її було видно поверх синьої
    plt.plot(data_xls['x'], data_xls['y'], 'r--', linewidth=2, label='Дані з Excel (CSV)')

    # 6. Додаємо елементи оформлення
    plt.title('Візуалізація функції згасаючих коливань\ny = x*0.5*sin(3*x)')
    plt.xlabel('Вісь X (час або відстань)')
    plt.ylabel('Вісь Y (амплітуда)')
    plt.legend()
    plt.grid(True)

    # Додамо горизонтальну лінію на нулі для наочності
    plt.axhline(0, color='black', linewidth=0.5)

    # 7. Показуємо вікно з графіком
    plt.show()

except FileNotFoundError as e:
    print(
        f"Помилка: файл не знайдено. Переконайтеся, що файли '{file_from_python}' та '{file_from_spreadsheet}' знаходяться у тій самій теці.")
except Exception as e:
    print(f"Сталася помилка: {e}")