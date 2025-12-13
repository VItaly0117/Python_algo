def validate_numeric(func):
    def wrapper(*args, **kwargs):
        for arg in args:
            if not isinstance(arg, (int, float)):
                raise TypeError("Усі аргументи мають бути числами")
        return func(*args, **kwargs)
    return wrapper
