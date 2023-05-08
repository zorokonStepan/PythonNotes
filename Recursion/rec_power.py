def power(x, n):
    if n == 0:
        return 1
    if n < 0:
        return 1 / power(x, -n)
    if n % 2 == 0:
        return power(x, (n // 2)) * power(x, (n // 2))
    else:
        return power(x, (n - 1)) * x


if __name__ == "__main__":
    assert power(2, -10) == 0.0009765625
