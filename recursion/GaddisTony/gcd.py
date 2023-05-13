def get_gcd(x, y):
    if x < y:
        x, y = y, x

    if x % y == 0:
        return y
    return get_gcd(x, x % y)


if __name__ == '__main__':
    assert get_gcd(10, 2) == 2
    assert get_gcd(55, 13) == 1
    assert get_gcd(55, 15) == 5
    assert get_gcd(49, 28) == 7
