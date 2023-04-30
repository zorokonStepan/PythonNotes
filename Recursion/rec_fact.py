def fact(n):
    if n == 1:
        return 1
    return fact(n - 1) * n


if __name__ == "__main__":
    assert fact(1) == 1
    assert fact(3) == 6
    assert fact(10) == 3_628_800
