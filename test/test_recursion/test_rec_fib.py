from recursion.rec_fib import rec_fib


def test_rec_fib():
    assert rec_fib(3) == 2
    assert rec_fib(10) == 55
    assert rec_fib(15) == 610
    assert rec_fib(23) == 28657
    assert rec_fib(30) == 832040
