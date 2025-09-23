def is_card_number_valid(numer: int | str) -> bool:
    """
        Проверяет, валиден ли номер кредитной карты, используя алгоритм Луна.

        Args:
            numer (int | str): Номер карты в виде целого числа или строки.

        Returns:
            bool: True, если номер карты валиден, иначе False.
        """
    if not isinstance(numer, (int, str)) or not str(numer).isdigit():
        return False

    number_str: str = str(numer)[::-1]
    sum_even: int = 0
    sum_odd: int = 0
    for e, digit in enumerate(number_str):
        digit_int = int(digit)
        if e % 2 == 0:
            sum_even += digit_int
        else:
            double_digit: int = digit_int * 2
            if double_digit > 9:
                double_digit -= 9
            sum_odd += double_digit

    total_sum: int = sum_even + sum_odd
    return total_sum % 10 == 0
