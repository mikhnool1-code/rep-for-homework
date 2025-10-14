a = "qwertyuiop[asdfghjkl"
symbol_1 = a[0]
symbol_2 = a[-1]
symbol_3 = a[2]
symbol_4 = a[-3]
a_length = len(a)
a_reverse = a[::-1]
symbol_8 = a[0:8]

assert len(a) >= 15, "Строка должна содержать не менее 15 символов"
assert symbol_1 == a[0], "Ошибка в первом символе"
assert symbol_2 == a[-1], "Ошибка в последнем символе"
assert symbol_3 == a[2], "Ошибка в третьем символе с начала"
assert symbol_4 == a[-3], "Ошибка в третьем символе с конца"
assert a_length == len(a), "Ошибка при вычислении длины строки"
assert a_reverse == a[::-1], "Ошибка при переворачивании строки"
assert symbol_8 == a[:8], "Ошибка при извлечении первых 8 символов"
