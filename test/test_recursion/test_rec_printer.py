from recursion.GaddisTony.rec_printer import rec_printer


def test_rec_printer():
    assert rec_printer(1) == "must be 2 args, but given 1"
    assert rec_printer(1, 2, 3) == "must be 2 args, but given 3"
    assert rec_printer(3, 1) == "No valid priority of args"
    assert rec_printer(1, '2') == "args must be <class 'int'>, but given <class 'str'>"
    assert rec_printer(1, 3.1) == "args must be <class 'int'>, but given <class 'float'>"
