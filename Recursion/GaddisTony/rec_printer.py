def is_valid_type_args(func):
    def wrapper(*args):
        for arg in args:
            type_arg = type(arg)
            if type_arg != int:
                return f"args must be <class 'int'>, but given {type_arg}"
        return func(*args)
    return wrapper


def is_valid_count_args(func):
    def wrapper(*args):
        len_args = len(args)
        if len_args != 2:
            return f"must be 2 args, but given {len_args}"
        return func(*args)
    return wrapper


def is_valid_priority(func):
    def wrapper(*args):
        if args[0] > args[1]:
            return 'No valid priority of args'
        return func(*args)
    return wrapper


@is_valid_count_args
@is_valid_type_args
@is_valid_priority
def rec_printer(start: int, stop: int):
    if start == stop:
        return print(stop)
    rec_printer(start, stop - 1)
    print(stop)


if __name__ == "__main__":
    assert rec_printer(1) == "must be 2 args, but given 1"
    assert rec_printer(1, 2, 3) == "must be 2 args, but given 3"
    assert rec_printer(3, 1) == "No valid priority of args"
    assert rec_printer(1, '2') == "args must be <class 'int'>, but given <class 'str'>"
    assert rec_printer(1, 3.1) == "args must be <class 'int'>, but given <class 'float'>"

    rec_printer(-100, 100)
