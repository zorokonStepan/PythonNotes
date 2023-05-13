from recursion.GaddisTony.rec_range_sum import rec_range_sum


def test_rec_range_sum():
    numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
    assert rec_range_sum(numbers) == 45
    assert rec_range_sum(numbers, 3) == 39
    assert rec_range_sum(numbers, 1, 5) == 14
