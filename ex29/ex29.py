# do you remember bro? Python and many languages like to return one of the operands to their Boolean expressions
# rather than just True or False. This means that if you did False and 1 you get the first operand (False),
# but if you do True and 1 you get the second (1).
# it tend to return the second operand: if it is definitely False, it yield False, if it's True, it yields the second operand
#print(True and 1)
#print(1 and True) # examples
# and remember that a and b evaluates consequentively, so if a already False, it won't evaluate b
# so as in a or b if a is True, b won't be evaluated
# everything is written bro, just use
people = 20
cats = 30
dogs = 15


if people < cats:
    print("Too many cats! The world is doomed!")

if people > cats:
    print("Not many cats! The world is saved!")

if people < dogs:
    print("The world is drooled on!")

if people > dogs:
    print("The world is dry!")


dogs += 5

if people >= dogs:
    print("People are greater than or equal to dogs.")

if people <= dogs:
    print("People are less that or equal to dogs.")


if people == dogs:
    print("People are dogs.")

if people or dogs:
    print("It will be executed")
    lol = 0
    if lol and dogs:
        print("It won't be executed")
# indentation make a command block
# 1 is True, 0 is False, as in Clang, 0 is false and every non-zero value is True
# but it's better to use True False notation, of course