def return_number (func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if not isinstance(result, (int, float)):
            raise ValueError("Arguments should be a number")
        return result
    return wrapper

@return_number
def arguments_summary(a, b):
    return a + b

@return_number
def concat_str(*args, **kwargs):
    if args:
        if all(isinstance(arg, str) for arg in args):
            return ''.join(args)

    if kwargs and "a" in kwargs:
        return kwargs["a"]

    return 0
