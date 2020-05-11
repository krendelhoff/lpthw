# this one is like your scripts with argv
# it seems like if you send multiple arguments, *args notation will make a list of it
# it's actually tuple.
# or a list. Gonna check this out later.
# *args is like argv but for functions
def print_two(*args):
    arg1, arg2 = args
    # unpacking args
    print(f"arg1: {arg1}, arg2: {arg2}")

# ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

# this just takes one argument
def print_one(arg1):
    print(f"arg1: {arg1}")

# this one takes no arguments
def print_none():
    print("I got nothin'.")

# in function and variable names you can use characters, numbers and underscores, but do not start with a number
def checklist():
    print("Checking my skills")

print_two("Zed", "Shaw")
print_two_again("Zed", "Shaw")
print_one("First!")
print_none()
checklist()