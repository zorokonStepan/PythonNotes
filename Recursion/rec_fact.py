def fact(num):
    if num < 0:
        return None
    if num in (0, 1):
        return 1
    return fact(num - 1) * num


if __name__ == "__main__":
    assert fact(1) == 1
    assert fact(3) == 6
    assert fact(10) == 3_628_800
