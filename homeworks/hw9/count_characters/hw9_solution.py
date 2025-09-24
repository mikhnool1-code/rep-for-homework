def count_char(raw_str):
    if not raw_str:
        return ""

    result = []
    counter = 1

    for i in range(1,len(raw_str)):
        if raw_str[i] == raw_str[i - 1]:
            counter += 1
        else:
            result += raw_str[i - 1]
            if counter > 1:
                result += str(counter)
            counter = 1

    result += raw_str[-1]
    if counter > 1:
        result += str(counter)

    return ''.join(result)
