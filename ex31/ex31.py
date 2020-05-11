# if statememt allow us to make decisions
# once more if, all the elif and else are mutually exclusive.
print("""You enter a dark room with two doors.
Do you go through door #1 or door #2?""")
print("OR THE DOOOOOOOOOOOOOOOOOOR NUMBER THREE???")

door = input("> ")

# here is presented idea of nested decisions
if door == "1":
    print("There's a giant bear here eating a cheese cake.")
    print("What do you do?")
    print("1. Take the cake.")
    print("2. Scream at the bear.")

    bear = input("> ")

    if bear == "1":
        print("The bear eats you face off. Good job!")
    elif bear == "2":
        print("The bear eats you legs off. Good job!")
    else:
        print(f"Well, doing {bear} is probably better.")

elif door == "2": # You can and actually should make a empty lines between such blocks, it's not rectricted
    print("You stare into the endless abyss at Cthulhu's retina.")
    print("1. Blueberries.")
    print("2. Yellow jacket clothespins.")
    print("3. Understading revolvers yelling melodies.")

    insanity = input("> ")

    if insanity == "1" or insanity == "2":
        print("Your body survives powered by a mind of jello.")
        print("Good job!")
    else:
        print("The insanity sots your eyes into a pool of muck.")
        print("Good job!")
elif door == "3":
    print("Wow man, you are not the stupid one.")
    print("It's the great decision.")
    print("But that's not enough to survive.")
    print("One more decision will define your destiny.")
    print("Choose wisely:")
    print("1. Vim")
    print("2. Emacs")
    editor = input("> ")

    if editor == "1":
        print("I have never doubted you.")
        print("You can go home.")
    else:
        print("Well....")
        print("*You died.*")
    

else:
    print("You stumble around and fall on a knife and die. Good job!")