def missing_statues(arr: list) -> int:
    existing_statues = sorted(arr)
    empty_list = []
    for e in range(len(existing_statues) - 1):
        diff = existing_statues[e + 1] - existing_statues[e]
        if diff > 1:
            empty_list.extend(range(existing_statues[e] + 1, existing_statues[e + 1]))
    return len(empty_list)


