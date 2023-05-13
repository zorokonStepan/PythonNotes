from recursion.rec_palindrome import rec_palindrome


def test_rec_palindrome():
    assert rec_palindrome('шалаш') is True
    assert rec_palindrome('йцйй') is False
