def find_square(a):
    return a * a


def check_even(b):
    return b % 2 == 0

assert find_square(2) == 4
assert find_square(5) == 25
assert check_even(2) is True
assert check_even(7) is False
