def validate_arguments(func):
    def wrapper(*args, **kwargs):
        for arg in args:
            if not isinstance(arg, (int, float)) or arg <= 0:
                raise ValueError(f"{arg} is not a positive")

        for arg in kwargs.values():
            if not isinstance(arg, (int, float)) or arg <= 0:
                raise ValueError(f"{arg} is not a positive")

        return func(*args, **kwargs)
    return wrapper


@validate_arguments
def sum_positive(*args, **kwargs):
    return sum(args) + sum(kwargs.values())
