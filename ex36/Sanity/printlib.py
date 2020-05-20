from time import sleep
from sys import exit


def prints(what, sec):

    print(what)
    sleep(sec)

def print_term(what):

    for c in what:

        print(c, end="", flush=True)
        sleep(0.1)

    print()


def dead(why):

    print(why)
    print("Bad end!")

    exit(0)
    