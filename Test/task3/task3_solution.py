def sum_numbers(n):
    total = sum(range(1, n + 1))
    expected = n * (n + 1) // 2

    assert total == expected, f"Ошибка: ожидалось {expected}, а получено {total}"

    return total


assert sum_numbers(1) == 1
assert sum_numbers(8) == 36
assert sum_numbers(22) == 253
assert sum_numbers(100) == 5050
