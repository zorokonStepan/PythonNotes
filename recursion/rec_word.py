def rec_word(sequence):
    if 0 < len(sequence) < 3:
        return sequence
    return sequence[0] + '(' + rec_word(sequence[1:-1]) + ')' + sequence[-1]
