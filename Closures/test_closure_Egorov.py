def main_func(name):
    def inner_func():
        return f'Hello my friend, {name}'
    return inner_func


def test_main_func():
    outer = main_func('Sam')
    assert outer() == 'Hello my friend, Sam'
    assert outer() != 'Hello my friend, SaM'
