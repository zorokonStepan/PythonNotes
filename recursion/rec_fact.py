def rec_fact(num):
    if num < 0:
        return None
    if num in (0, 1):
        return 1
    return rec_fact(num - 1) * num
