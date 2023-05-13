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
    rec_printer(-100, 100)
