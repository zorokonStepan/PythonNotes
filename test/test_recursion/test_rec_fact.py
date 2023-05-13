from recursion.rec_fact import rec_fact


def test_rec_fact():
    assert rec_fact(1) == 1
    assert rec_fact(3) == 6
    assert rec_fact(10) == 3_628_800
