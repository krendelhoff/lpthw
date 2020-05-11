people = 30
cars = 40
trucks = 15


# an if statement creates a branch in the code
# in if could be any boolean expression with arbitrary complexity, although complex expressions are usually bad style
# if expression is True the block will be executed
if cars > people:
    print("We should take the cars.")
elif cars < people:
    print("We should not take the cars.")
else:
    print("We can't decide.")

# if else blocks are mutually exclusive, remember it - only one block will be executed
if trucks > cars:
    print("That's too many trucks.")
elif trucks < cars:
    print("Maybe we could take the trucks.")
else:
    print("We still can't decide.")

if people > trucks:
    print("Alright, let's just take the trucks.")
else:
    print("Fine, let's stay home then.")
    
critical_amount = 50
if people > critical_amount:
    print("No! There is too much people. Time to become vegan.")
elif people == critical_amount:
    print("We are walking on the edge.")
else:
    print("Everything is fine.")