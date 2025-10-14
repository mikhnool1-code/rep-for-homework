A = "qwertyuiop[asdfghjkl"
SYMBOL_1 = A[0]
SYMBOL_2 = A[-1]
SYMBOL_3 = A[2]
SYMBOL_4 = A[-3]
A_LENGTH = len(A)
A_REVERSE = A[::-1]
SYMBOL_8 = A[0:8]


assert len(A) >= 15, "Строка должна содержать не менее 15 символов"
assert SYMBOL_1 == A[0], "Ошибка в первом символе"
assert SYMBOL_2 == A[-1], "Ошибка в последнем символе"
assert SYMBOL_3 == A[2], "Ошибка в третьем символе с начала"
assert SYMBOL_4 == A[-3], "Ошибка в третьем символе с конца"
assert A_LENGTH == len(A), "Ошибка при вычислении длины строки"
assert A_REVERSE == A[::-1], "Ошибка при переворачивании строки"
assert SYMBOL_8 == A[:8], "Ошибка при извлечении первых 8 символов"
