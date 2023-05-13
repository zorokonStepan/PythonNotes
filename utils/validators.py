from functools import wraps


def is_valid_count_args(count_args: int):
    def decorator(func):
        @wraps(func)
        def wrapper(*args):
            len_args = len(args)
            if len_args != count_args:
                return f"must be {count_args} args, but given {len_args}"
            return func(*args)
        return wrapper
    return decorator


def is_valid_type_args(func):
    def wrapper(*args):
        for arg in args:
            type_arg = type(arg)
            if type_arg != int:
                return f"args must be <class 'int'>, but given {type_arg}"
        return func(*args)
    return wrapper


def is_valid_priority(func):
    def wrapper(*args):
        if args[0] > args[1]:
            return 'No valid priority of args'
        return func(*args)
    return wrapper
