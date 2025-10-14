def string_reverse(str_name, n):
    result = ""

    for i in range(n):
        result += str_name[i]

    for i in range(n - 2, -1, -1):
        result += str_name[i]

    return result


S = "abcdefghlfmvkfnvmCVEKEAVM"


assert string_reverse(s, 1) == "a"
assert string_reverse(s, 2) == "aba"
assert string_reverse(s, 3) == "abcba"
assert string_reverse(s, 4) == "abcdcba"
