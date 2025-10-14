def decorator(*d_args, **d_kwargs):
    def real_decorator(func):
        def wrapper(*args, **kwargs):
            print((d_args, d_kwargs))
            return func(*args, **kwargs)
        return wrapper
    return real_decorator


@decorator(1, 2, 3, [1, 2, 3], 'one', 'two', 'three', one=1, two=2, three=3)
def identity(x):
    return x


@decorator()
def identity_empty(x):
    return x


print(identity(42))
print(identity_empty(42))


assert identity(100) == 100
assert identity_empty('hi') == 'hi'
assert callable(identity)
assert callable(identity_empty)
