class Girlfriend:
    def __init__(self, initial_budget):
        # Приватне поле (Інкапсульовані дані), доступ контролюється
        self.__secret_budget = initial_budget
    def do_make_up(self):
        print("Соня зробила макіяж")
    # --- Методи для контрольованого доступу до приватного поля ---
    # Геттер: Дозволяє прочитати приватний стан
    def check_wallet(self):
        return f"У Соні залишилося {self.__secret_budget} грн."

    # Сеттер: Дозволяє змінити приватний стан, але з перевіркою
    def buy_clothes(self, item_price):
        if item_price <= self.__secret_budget:
            self.__secret_budget -= item_price
            print(f"Куплено одяг за {item_price} грн. Залишок: {self.__secret_budget} грн.")
        else:
            print("Недостатньо коштів! Потрібно більше грошей для покупки.")
# --- Використання Інкапсуляції ---
Sonya = Girlfriend(initial_budget=5000)
# Читання інкапсульованих даних через публічний метод
print(Sonya.check_wallet())  # Виведе: У Соні залишилося 5000 грн.
# Контрольована зміна інкапсульованих даних
Sonya.buy_clothes(item_price=3000)  # Покупка дозволена
Sonya.buy_clothes(item_price=4000)  # Покупка заборонена через умову в методі
# Спроба прямого доступу до приватного поля призведе до помилки (Або до Name Mangling)
# print(Sonya.__secret_budget)