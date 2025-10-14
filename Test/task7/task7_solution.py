def string_reverse(s, n):
    result = ""

    for i in range(n):
        result += s[i]

    for i in range(n - 2, -1, -1):
        result += s[i]

    return result


s = "abcdefghlfmvkfnvmCVEKEAVM"

assert string_reverse(s, 1) == "a"
assert string_reverse(s, 2) == "aba"
assert string_reverse(s, 3) == "abcba"
assert string_reverse(s, 4) == "abcdcba"
