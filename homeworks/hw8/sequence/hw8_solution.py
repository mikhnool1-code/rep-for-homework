def is_almost_sorted(arr: list) -> bool:
    for i in range(len(arr) - 1):
        if arr[i] >= arr[i + 1]:
            return False
    return True

def ascending_sequence(arr: list) -> bool:
    if is_almost_sorted(arr):
        return True

    for i in range(len(arr)):
        new_lst = arr[:i] + arr[i + 1:]

        if is_almost_sorted(new_lst):
            return True

    return False
