import os
import time
import multiprocessing


def whoami(name):
    print("I'm %s, in process %s" % (name, os.getpid()))


def loopy(name):
    whoami(name)

    start = 1
    stop = 1_000_000

    for num in range(start, stop):
        print("\tNumber %s of %s. Honk!" % (num, stop))
        time.sleep(1)


if __name__ == "__main__":
    whoami("main")
    p = multiprocessing.Process(target=loopy, args=("loopy",))
    p.start()
    time.sleep(5)
    p.terminate()


# I'm main, in process 17100
# I'm loopy, in process 11332
# 	Number 1 of 1000000. Honk!
# 	Number 2 of 1000000. Honk!
# 	Number 3 of 1000000. Honk!
# 	Number 4 of 1000000. Honk!
# 	Number 5 of 1000000. Honk!
#
# Process finished with exit code 0
