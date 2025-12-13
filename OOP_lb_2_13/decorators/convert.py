def float_to_int(func):
    def wrapper(*args, **kwargs):
        new_args = []
        for arg in args:
            if isinstance(arg, float):
                new_args.append(int(arg))
            else:
                new_args.append(arg)

        return func(*new_args, **kwargs)
    return wrapper
