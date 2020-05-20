from time import sleep

def pr(what):

    print(what, end="", flush=True)


def prs(what):

    for c in what:
        pr(c)
        sleep(0.1)


while True:
    pr("Hello!")
    pr("\r")
    sleep(0.5)
    pr("      ")
    sleep(0.5)
    pr("\r")
    pr("Hello!")
    pr("\r")
print()