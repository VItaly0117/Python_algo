from functools import wraps


def validate_numeric(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Перевіряємо всі позиційні аргументи
        for arg in args:
            if not isinstance(arg, (int, float)):
                raise TypeError(f"Аргумент {arg} має бути числом")

        # Перевіряємо всі іменовані аргументи
        for key, value in kwargs.items():
            if not isinstance(value, (int, float)):
                raise TypeError(f"Аргумент '{key}' має бути числом")

        return func(*args, **kwargs)

    return wrapper