import numpy as np
from math import sqrt


# --- Декоратор для конвертації (Завдання 1.1) ---
def to_si_coulomb(func):
    """
    Декоратор для переведення результату з одиниць 10^-10 СГСЕ в Кулони.
    """

    def wrapper(self):
        val_esu_scaled = func(self)
        val_esu = val_esu_scaled * 1e-10
        # 1 esu ≈ 3.33564e-10 C
        conversion_factor = 3.33564e-10
        val_coulomb = val_esu * conversion_factor
        return val_coulomb

    return wrapper


# --- Клас для однієї вибірки (Завдання 1.1 та 1.2) ---
class SingleSampleAnalysis:
    def __init__(self, data_array, alpha=0.99):
        self.data = data_array
        self.n = len(data_array)
        self.alpha = alpha

        # Розрахунки [cite: 6-13]
        self.XSR = self.calc_mean()
        self.VBSRX = self.calc_variance()
        self.SX = self.calc_std_sample()
        self.SigmaX = self.calc_sigma_error()

        # Довірчий інтервал
        self.t_student = self.get_student_t(self.alpha)
        self.DeltaX = self.calc_absolute_error(self.t_student)

    def calc_mean(self):
        """Формула 1.1 [cite: 7]"""
        return np.mean(self.data)

    def calc_variance(self):
        """Формула 1.2 [cite: 9]"""
        return np.var(self.data, ddof=1)

    def calc_std_sample(self):
        """Формула 1.3 [cite: 11]"""
        return np.std(self.data, ddof=1)

    def calc_sigma_error(self):
        """Формула 1.4 [cite: 13]"""
        return self.SX / sqrt(self.n)

    def get_student_t(self, alpha):
        """Коефіцієнт Стьюдента (Таблиця 1.1) [cite: 66]"""
        if self.n > 30:
            if alpha == 0.99: return 2.66
            if alpha == 0.95: return 2.00
        else:
            # Для малих вибірок (як у завданні 1.2, n=8)
            if self.n == 8:
                if alpha == 0.99: return 3.499
                if alpha == 0.95: return 2.365
        return 2.0  # Значення за замовчуванням

    def calc_absolute_error(self, t_val):
        """Формула 2.6 [cite: 68]"""
        return self.SigmaX * t_val

    def get_interval_for_custom_alpha(self, custom_alpha):
        t = self.get_student_t(custom_alpha)
        delta = self.calc_absolute_error(t)
        return t, delta

    @to_si_coulomb
    def get_result_si(self):
        return self.XSR


# --- Клас для кореляційного аналізу (Завдання 1.3) ---
class TwoSampleAnalysis:
    def __init__(self, x_array, y_array):
        if x_array.shape != y_array.shape:
            raise ValueError("Масиви повинні бути використанні однакової довжини")

        self.x = x_array
        self.y = y_array
        self.n = len(x_array)

        # Розрахунки для X та Y
        self.XSR = self.calc_mean(self.x)
        self.VBSRX = self.calc_variance(self.x)
        self.SX = self.calc_std(self.x)
        self.SigmaX = self.calc_sigma(self.SX)

        self.YSR = self.calc_mean(self.y)
        self.VBSRY = self.calc_variance(self.y)
        self.SY = self.calc_std(self.y)
        self.SigmaY = self.calc_sigma(self.SY)

        # Кореляція [cite: 89]
        self.R = self.calc_correlation()

    def calc_mean(self, arr):
        return np.mean(arr)

    def calc_variance(self, arr):
        """Формула 2.8, 2.9 [cite: 91, 92]"""
        return np.var(arr, ddof=1)

    def calc_std(self, arr):
        return np.std(arr, ddof=1)

    def calc_sigma(self, std_val):
        return std_val / sqrt(self.n)

    def calc_correlation(self):
        """Формула 2.7 [cite: 89]"""
        numerator = np.sum((self.x - self.XSR) * (self.y - self.YSR))
        denominator = (self.n - 1) * self.SX * self.SY
        return numerator / denominator


# --- Клас для генерації звітів (ЗМІНЕНО) ---
class Report:
    @staticmethod
    def print_single_sample(experiment, precision=4):
        """
        Виводить звіт для однієї вибірки.
        :param precision: Кількість знаків після коми (int)
        """
        p = precision  # коротка назва для зручності у f-рядках

        print("-" * 50)
        print(f"ЗВІТ: Аналіз однієї вибірки (n={experiment.n})")
        print("-" * 50)
        # Використовуємо :.{p}f для динамічної підстановки точності
        print(f"Середнє (XSR):             {experiment.XSR:.{p}f}")
        print(f"Дисперсія (VBSRX):         {experiment.VBSRX:.{p}f}")
        print(f"СКВ вибірки (SX):          {experiment.SX:.{p}f}")
        print(f"СК похибка (SigmaX):       {experiment.SigmaX:.{p}f}")

        # Для СІ використовуємо наукову нотацію (.4e), бо числа дуже малі
        if hasattr(experiment, 'get_result_si'):
            print(f"Значення в СІ:             {experiment.get_result_si():.4e}")

        print(f"Довірчий інтервал (a={experiment.alpha}):")
        print(f"  {experiment.XSR:.{p}f} ± {experiment.DeltaX:.{p}f}")
        print("-" * 50 + "\n")

    @staticmethod
    def print_correlation(experiment, precision=4):
        """
        Виводить звіт кореляційного аналізу.
        :param precision: Кількість знаків після коми (int)
        """
        p = precision

        print("-" * 50)
        print(f"ЗВІТ: Кореляційний аналіз (n={experiment.n})")
        print("-" * 50)
        print(f"{'Параметр':<15} | {'X':<10} | {'Y':<10}")
        print("-" * 40)
        print(f"{'Середнє':<15} | {experiment.XSR:<10.{p}f} | {experiment.YSR:<10.{p}f}")
        print(f"{'Дисперсія':<15} | {experiment.VBSRX:<10.{p}f} | {experiment.VBSRY:<10.{p}f}")
        print(f"{'СКВ (S)':<15} | {experiment.SX:<10.{p}f} | {experiment.SY:<10.{p}f}")
        print("-" * 40)
        print(f"Коефіцієнт кореляції (r): {experiment.R:.{p}f}")

        strength = "слабкий"
        if abs(experiment.R) > 0.7: strength = "сильний"
        if abs(experiment.R) > 0.9: strength = "дуже сильний"
        print(f"Зв'язок: {strength}")
        print("-" * 50 + "\n")


# --- Main Execution ---
if __name__ == "__main__":
    # --- Завдання 1.1 ---
    # Дані [cite: 107-114]
    data_millikan = np.array([
        4.781, 4.764, 4.777, 4.809, 4.761, 4.769, 4.772, 4.764,
        4.795, 4.776, 4.765, 4.790, 4.792, 4.806, 4.785, 4.788,
        4.769, 4.771, 4.785, 4.779, 4.758, 4.779, 4.799, 4.749,
        4.792, 4.789, 4.805, 4.788, 4.764, 4.785, 4.791, 4.774,
        4.779, 4.772, 4.768, 4.772, 4.810, 4.790, 4.783, 4.783,
        4.775, 4.789, 4.801, 4.791, 4.799, 4.777, 4.797, 4.781,
        4.782, 4.778, 4.808, 4.740, 4.790, 4.767, 4.791, 4.771,
        4.775, 4.747
    ])

    exp1 = SingleSampleAnalysis(data_millikan, alpha=0.99)
    # В завданні 1.1 просять округлити до тисячних, тому precision=3
    Report.print_single_sample(exp1, precision=3)

    # --- Завдання 1.2 ---
    # Дані [cite: 120]
    voltage_data = np.array([210, 205, 195, 200, 210, 220, 190, 210])
    exp2 = SingleSampleAnalysis(voltage_data, alpha=0.99)
    # Тут дані цілі числа, тому достатньо precision=2
    Report.print_single_sample(exp2, precision=2)

    # Додатковий вивід для 1.2 (a=0.95) згідно умови [cite: 122]
    t_95, d_95 = exp2.get_interval_for_custom_alpha(0.95)
    print(f"Додатково для 1.2 (a=0.95): {exp2.XSR:.2f} ± {d_95:.2f} В\n")

    # --- Завдання 1.3 ---
    # Дані [cite: 135, 137]
    temp_x = np.array([0, 50, 100, 150, 200, 300, 400, 500, 600, 700])
    strength_y = np.array([23.3, 21.0, 19.2, 16.4, 15.5, 13.3, 9.4, 5.9, 4.1, 1.9])

    exp3 = TwoSampleAnalysis(temp_x, strength_y)
    Report.print_correlation(exp3, precision=3)
