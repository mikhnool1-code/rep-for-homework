def remove_previous_symbol(raw_str):
    empty_list:list = []
    for e in raw_str:
        if e != "#":
            empty_list.append(e)
        elif empty_list:
            empty_list.pop()
    return "".join(empty_list)
