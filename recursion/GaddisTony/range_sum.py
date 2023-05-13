def range_sum(sequence, start=None, end=None):
    if sequence:
        end = len(sequence) if (end is None) else end
        start = 0 if (start is None) else start

        if start >= end:
            return 0
        return sequence[start] + range_sum(sequence, start + 1, end)

    return None


if __name__ == "__main__":
    numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
    assert range_sum(numbers) == 45
    assert range_sum(numbers, 3) == 39
    assert range_sum(numbers, 1, 5) == 14
