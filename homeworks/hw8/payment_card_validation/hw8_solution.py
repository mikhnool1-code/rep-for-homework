def is_card_number_valid(numer) -> bool:
    if not isinstance(numer, (int, str)) or not str(numer).isdigit():
        return False

    number_str = str(numer)[::-1]
    sum_even = 0
    sum_odd = 0
    for e, digit in enumerate(number_str):
        digit = int(digit)
        if e % 2 == 0:
            sum_even += digit
        else:
            double_digit = digit * 2
            if double_digit > 9:
                double_digit -= 9
            sum_odd += double_digit

    total_sum = sum_even + sum_odd
    return total_sum % 10 == 0
