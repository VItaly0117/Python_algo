def clamp_result(min_val, max_val):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)

            if result < min_val:
                return min_val
            if result > max_val:
                return max_val

            return result
        return wrapper
    return decorator
