def add(a, b):
    print(f"ADDING {a} + {b}")
    return a + b

def subtract(a, b):
    print(f"SUBTRACTING {a} - {b}")
    return a - b

def multiply(a, b):
    print(f"MULTIPLYING {a} * {b}")
    return a * b

def divide(a, b):
    print(f"DIVIDING {a} / {b}")
    return a // b

print("Let's do some math with just functions!")

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)
# return keyword replace the function call by a return value. You don't have to assign that value.
# you can return anything that you can put after the = 
# From now, in every your code, in C or Java or whatever, use comments

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")



# A puzzle for the extra credit, type it in anyway.
print("Here is a puzzle")

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))
# functions return values, so we can call them even inside call of another function(as arguments)
# once more - we use the return value of one function as an argument to another function call
# using the script output you can actually see the order of function calling (it's pretty logical)
where = subtract(add(10, 20), add(multiply(20, 3484782 * divide(954387593485743, 483294)), 10))
# I can't understand how by now, but there is no limit for the integer range in python
# functions calls inside out
# You also can do something like this: funcall(float(input()), 249394) and everything will be fine
wow = subtract(float(input("Enter the value, from where will be subracted 10: ")), 10)
print("That's that value:", wow)

print("That becomes:", what, "Can you do it by hand?")

print("That becomes:", where)
print("...")
print("вот и сиди гадай терь долбан)")