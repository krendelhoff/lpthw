from sys import argv

def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket.\n")

def function(n):
    print(n // 10)

# Variables in functions is private for that function: you can use exactly same name outside it
# and function also takes argument by value, as in Clang
print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)
# As you remember about scope, if you create the variable with the same name in the function, it replaces the external one
# It's bad practive to have the same global and automatic variable names


print("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)


print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)


print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

function(10)
a = 20
function(a)
function(10 + 1)
function(a + 10)
function((a + 49324739847) // 10)
script, value = argv
value = int(value)
function(value)
function(value - a)
function(10 * a / 10)
function(113948 % 348)
function(int(input("Enter the number: ")))
function(20 + 20 + 20 + 20)
