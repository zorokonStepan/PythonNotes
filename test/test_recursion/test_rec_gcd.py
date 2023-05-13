from recursion.GaddisTony.rec_gcd import rec_gcd


def test_rec_gcd():
    assert rec_gcd(10, 2) == 2
    assert rec_gcd(55, 13) == 1
    assert rec_gcd(55, 15) == 5
    assert rec_gcd(49, 28) == 7
