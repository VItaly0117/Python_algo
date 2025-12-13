from functools import wraps

def clamp_result(min_val, max_val):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            # Елегантне обмеження діапазону
            return max(min_val, min(result, max_val))
        return wrapper
    return decorator