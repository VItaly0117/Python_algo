class Appliance:
    def __init__(self, name, power_watts):
        self.name = name
        self.power_watts = power_watts # Потужність у Ватах
        self.is_active = False         # За замовчуванням вимкнено

    def turn_on(self):
        self.is_active = True
        print(f"[INFO] {self.name} увімкнено.")

    def turn_off(self):
        self.is_active = False
        print(f"[INFO] {self.name} вимкнено.")

class SmartHouse:
    def __init__(self, tariff):
        self.devices = []
        self.tariff = tariff # Ціна за 1 кВт*год (наприклад, 4.32 грн)

    def add_device(self, device):
        self.devices.append(device)

    def get_total_power(self):
        """Повертає сумарну потужність лише УВІМКНЕНИХ приладів (у Вт)"""
        total = 0
        for dev in self.devices:
            if dev.is_active:
                total += dev.power_watts
        return total

    def calculate_cost(self, hours):
        """
        Розраховує вартість роботи увімкнених приладів за передану кількість годин.
        Формула: (Потужність (Вт) / 1000) * Години * Тариф
        """
        total_watts = self.get_total_power()
        kilowatts = total_watts / 1000
        cost = kilowatts * hours * self.tariff
        return cost

# --- Демонстрація ---

# 1. Створюємо будинок з тарифом 4.32 грн за кВт
my_home = SmartHouse(tariff=4.32)

# 2. Створюємо прилади
tv = Appliance("Телевізор", 150)
kettle = Appliance("Електрочайник", 2000)
fridge = Appliance("Холодильник", 300)
lamp = Appliance("Люстра", 60)

# 3. Додаємо їх у систему
my_home.add_device(tv)
my_home.add_device(kettle)
my_home.add_device(fridge)
my_home.add_device(lamp)

print("--- Початок симуляції ---")

# 4. Вмикаємо деякі прилади
tv.turn_on()
lamp.turn_on()
fridge.turn_on()
# Чайник залишаємо вимкненим

# 5. Розрахунок
current_load = my_home.get_total_power()
hours_active = 5 # Уявимо, що це все працювало 5 годин

bill = my_home.calculate_cost(hours_active)

print("-" * 30)
print(f"Зараз працюють прилади загальною потужністю: {current_load} Вт")
print(f"За {hours_active} годин роботи набіжить сума: {bill:.2f} грн")