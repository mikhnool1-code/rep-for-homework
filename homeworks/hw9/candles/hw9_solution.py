def count_candles(candles, leftover):
    total_burned = candles
    current_leftover = candles

    while current_leftover >= leftover:
        new_candles = current_leftover // leftover
        total_burned += new_candles
        current_leftover = current_leftover % leftover + new_candles
    return total_burned
