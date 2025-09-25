def level_up(experience: int, threshold: int, reward: int) -> bool:
    new_experience = experience + reward
    return new_experience >= threshold


def motor_time(n: int) -> int:
    hours = n // 60
    minutes = n % 60
    total_sum = sum(int(digit) for digit in f"{hours:02}{minutes:02}")
    return total_sum


def time_converter(time_str: str) -> str:
    hours, minutes = map(int, time_str.split(':'))
    if hours == 0:
        period = 'a.m.'
        hours_12 = 12
    elif 1 <= hours <= 11:
        period = 'a.m.'
        hours_12 = hours
    elif hours == 12:
        period = 'p.m.'
        hours_12 = 12
    else:
        period = 'p.m.'
        hours_12 = hours - 12
    return f"{hours_12}:{minutes:02} {period}"
