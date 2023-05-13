from utils.validators import is_valid_count_args, is_valid_type_args, is_valid_priority


@is_valid_count_args(2)
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
