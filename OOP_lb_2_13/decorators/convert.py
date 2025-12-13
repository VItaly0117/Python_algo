from functools import wraps


def float_to_int(func):
    @wraps(func)  # Зберігає метадані функції
    def wrapper(*args, **kwargs):
        # Обробка позиційних аргументів
        new_args = [int(arg) if isinstance(arg, float) else arg for arg in args]

        # Обробка іменованих аргументів
        new_kwargs = {k: (int(v) if isinstance(v, float) else v) for k, v in kwargs.items()}

        return func(*new_args, **new_kwargs)

    return wrapper