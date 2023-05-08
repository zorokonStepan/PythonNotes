def tower_of_hanoi(num, from_req, to_req, tmp_req):
    if num > 0:
        tower_of_hanoi(num - 1, from_req, tmp_req, to_req)
        print(f'Переместить кольцо со стержня {from_req} на стержень {to_req}')
        tower_of_hanoi(num - 1, tmp_req, to_req, from_req)


if __name__ == '__main__':
    tower_of_hanoi(3, 1, 3, 2)
