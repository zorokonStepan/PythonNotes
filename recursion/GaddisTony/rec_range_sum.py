def rec_range_sum(sequence, start=None, end=None):
    if sequence:
        end = len(sequence) if (end is None) else end
        start = 0 if (start is None) else start

        if start >= end:
            return 0
        return sequence[start] + rec_range_sum(sequence, start + 1, end)

    return None
