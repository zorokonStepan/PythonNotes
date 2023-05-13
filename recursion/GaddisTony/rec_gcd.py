def rec_gcd(x, y):
    if x < y:
        x, y = y, x

    if x % y == 0:
        return y
    return rec_gcd(x, x % y)
