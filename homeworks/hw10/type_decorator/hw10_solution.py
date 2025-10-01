def typed(element):
    def decorator(func):
        def wrapper(*args):
            converted_args = map(element, args)
            return func(*converted_args)
        return wrapper
    return decorator


@typed(element=str)
def add_str(*args):
    return ''.join(args)


@typed(element=int)
def add_int(*args):
    return sum(args)


@typed(element=float)
def add_float(*args):
    total_sum = 0
    for arg in args:
        total_sum += arg
    return total_sum
