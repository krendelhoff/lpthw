# IF YOU TYPE A BUITIN FUNCTION NAME IN PRINT IT WILL GIVE INFO ABOUT IT
# also in python shell if you type some func name it will display info about it
# for iterate a variable into a list or something
# while do the job while the condition is True
# everything after :  and indented is a code block
# for loop in Python is much more powerful than in C
numbers = list()

# Look, in functions you can't use the external variables. Or can. Find out that later.
def init(numbers, n, inc):
    i = 0
    while i < n:
        print(f"At the top i is {i}")
        numbers.append(i)

        i += inc
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")

def init2(numbers, n):
    for i in range(n):
        print(f"At the top i is {i}")
        numbers.append(i)
        i += 5945984
        # LOOK. You can't affect the i, because it defines and initializes again and again every iteration.
        # do not assign. Initialize to the next value. So the old value is gone. It's empty and it is initialized.
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")

init2(numbers, 8)

print("The numbers: ")

for num in numbers:
    print(num)
