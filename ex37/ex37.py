import sys
try:
    sys.exit(0)
except SystemExit:
    print('Meow')
# Exceptions is that errors you get when your program goes wrong and you can process them.
# You process them using try except else finally constructions.
# You can work out every error and not let your program stop working.
# Again, every error that stop program is actually exception. Read about it and work out later.
# @ is just a decorator.
# Read about OOP man. And exceptions.
try:
    assert(False)
except AssertionError:
    print("Meow2")
finally:
    print("You know how to work with exceptions in Python.")
    print("Revise that tables you did today.")