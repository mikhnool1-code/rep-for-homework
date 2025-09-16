import random


def check_guess(hidden_number : str, user_number: str) -> tuple[int, int]:
    result1 = []
    result2 = []
    # hidden_number = random.randint(1000, 9999)
    # guess = input("Введите 4-х значное число: ")
    user_iterator = 0
    # while hidden_number != guess:
    for u in user_number:
        hidden_iterator = 0
        for e in hidden_number:
            if u == e:
                if user_iterator == hidden_iterator:
                    result2.append(u)
                    break
                else:
                    result1.append(u)
                    break
            hidden_iterator +=1
        user_iterator +=1

    # if len(result1) == 0:
    #     return ("Вы проиграли! :(")
    # if len(result2) == 4:
    #     return ("Вы выиграли!")
    #
    # result_string = ""
    # if len(result1) != 0:
    #     result_string = (len(result1) + "коровы")
    # if len(result2) != 0:
    #     result_string = result_string + (len(result1) + "бык")

    return (len(result2), len(result1))


def generate_secret_number() -> str:
    unique_digits = random.sample("0123456789", 4)
    return ''.join(unique_digits)



