def validation(func):
    def wrapper(*args):
        for arg in args:
            if type(arg) != int:
                return False
        func(*args)
    return wrapper


@validation
def printer(start: int, stop: int):
    print(start, stop)


printer(1, '2')
