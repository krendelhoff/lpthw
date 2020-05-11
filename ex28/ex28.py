print("1.", True and True, "True?") # True
print("2.", False and True, "False?") # False
print("3.", 1 == 1 and 2 == 1, "False?") # False
print("4.", "test" == "test", "True?") # True
print("5.", 1 == 1 or 2 != 1, "True?") # True
print("6.", True and 1 == 1, "True?") # True
print("7.", False and 0 != 0, "False?") # False
print("8.", True or 1 == 1, "True?") # True
print("9.", "test" == "testing", "False?") # False
print("10.", 1 != 0 and 2 == 1, "False?") # False
print("11.", "test" != "testing", "True?") # True
print("12.", "test" == 1, "False?") # False
print("13.", not(True and False), "True?") # True
print("14.", not(1 == 1 and 0 != 1), "False?") # False
print("15.", not(10 == 1 or 1000 == 1000), "False?") # False
print("16.", not(1 != 10 or 3 == 4), "False?") # False
print("17.", not("testing" == "testing" and "Zed" == "Cool Guy"), "True?") # True
print("18." , 1 == 1 and (not("testing" == 1 or 1 == 0)), "True?") # True
print("19.", "chunky" == "bacon" and (not(3 == 4 or 3 == 3)), "False?") # False
print("20.", 3 == 3 and (not("testing" == "testing" or "Python" == "Fun")), "False?") # False
a = 5
b = 6
print(f"a is b yields {a is b}")
print(f"a == b yields {a == b}")
# you are the best mathematical logic bro
# there also in and not in, and is and not is operators in python
# in is membership operator, checks if it is in list or tuple or whatever
# is is the identity operator - Identity operators compare the memory locations of two objects
# Evaluates to true if the variables on either side of the operator point to the same object and false otherwise.
# if point to the same object, not the equal, but same
# and such construction: with open(filename, 'r') as file: remember it bro 
# interesting thing "test" and "test" will yield "test", 1 and 1 will yield 1, python tends to return one of the operators
# not only True or False
