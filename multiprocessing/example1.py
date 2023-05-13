import os
import multiprocessing


def whoami(what):
    print("Process %s says: %s" % (os.getpid(), what))


if __name__ == "__main__":
    whoami("I'm the main program")
    for n in range(4):
        p = multiprocessing.Process(target=whoami, args=("I'm function %s" % n,))
        p.start()


# Process 13776 says: I'm the main program
# Process 14456 says: I'm function 0
# Process 16456 says: I'm function 1
# Process 7572  says: I'm function 2
# Process 12756 says: I'm function 3
