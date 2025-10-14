def plus_one(digits):
    for i in range(len(digits) - 1, -1, -1):
        if digits[i] < 9:
            digits[i] += 1
            return digits
        digits[i] = 0
    return [1] + digits

assert plus_one([9]) == [1, 0]
assert plus_one([1, 2, 3]) == [1, 2, 4]
assert plus_one([1, 1, 9]) == [1, 2, 0]
assert plus_one([9, 9, 9]) == [1, 0, 0, 0]
