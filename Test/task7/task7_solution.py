def string_reverse(str_name, n):
    result = ""

    tmp = str_name[:n]

    result += tmp[-2::-1]

    return result


S = "abcdefghlfmvkfnvmCVEKEAVM"


assert string_reverse(S, 1) == "a"
assert string_reverse(S, 2) == "aba"
assert string_reverse(S, 3) == "abcba"
assert string_reverse(S, 4) == "abcdcba"
