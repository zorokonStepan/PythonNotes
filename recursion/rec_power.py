def rec_power(x, n):
    if n == 0:
        return 1
    if n < 0:
        return 1 / rec_power(x, -n)
    if n % 2 == 0:
        return rec_power(x, (n // 2)) * rec_power(x, (n // 2))
    else:
        return rec_power(x, (n - 1)) * x
