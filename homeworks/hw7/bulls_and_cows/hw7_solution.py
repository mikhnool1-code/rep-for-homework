import random


def check_guess(hidden_number: str, user_number: str) -> tuple[int, int]:
    result1 = []
    result2 = []
    user_iterator = 0
    for u in user_number:
        hidden_iterator = 0
        for e in hidden_number:
            if u == e:
                if user_iterator == hidden_iterator:
                    result2.append(u)
                    continue
                else:
                    result1.append(u)
            hidden_iterator += 1
        user_iterator += 1

    return len(result2), len(result1)


def generate_secret_number() -> str:
    unique_digits = random.sample("0123456789", 4)
    return ''.join(unique_digits)
