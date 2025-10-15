def is_palindrome(x):

    if x < 0:
        return False

    s = str(x)
    if s == s[::-1]:
        return True

    return False


assert is_palindrome(121) is True
assert is_palindrome(-121) is False
assert is_palindrome(10) is False
assert is_palindrome(0) is True
assert is_palindrome(1001) is True
assert is_palindrome(100) is False
