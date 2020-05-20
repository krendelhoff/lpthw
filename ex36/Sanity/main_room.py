from time import sleep
from subprocess import call
from printlib import prints, print_term, dead
from header import name, prompt
from room2 import room2


def main_room():

    prints("*You entered the room, which consists of doors, and nothing anymore*", 2) 
    prints("*Doors are numbered in a very strange way. You have already seen something like this.*", 2)
    prints("*The first one and second one are numbered 1*", 2)
    prints("*The next one is 2, then 3, then 5, then 8.*", 2)
    prints("*From that point you can see there is 10 doors, and their numbers are 1, 1, 2, 3, 5, 8, 13, 21, 34, 55.*", 2)
    prints("*Suddenly, you see some kind of terminal.*", 2)

    print("What are you going to do?")

    opened = False
    destroyed = False

    while True:

        answer = input(prompt).lower()

        if "open terminal" in answer:

            if not destroyed:

                opened = term()

        elif "destroy terminal" in answer:

            destroyed = True
            print("*Terminal was destroyed without any chance to restore.*")

        elif "open" and "door" in answer:

            if destroyed:

                # you can do multiline arithmetic
                str1 = "The only possible outcome you had is to return to Jacque."\
                + "But that was worser than death, so you stayed"
                str2 = " in that room to the end of the centuries."
                str3 = " During that period your sanity was seriously corrupted."

                dead(str1 + str2 + str3)

            if not opened:

                print("Doors are locked.")

            elif "1" in answer:

                str1 = "You entered the door 1 and came back to the same room, but from another door marked 1. " 
                print(str1 + "Interesting trick from non-euclidian geometry.")

            elif "2" in answer:

                room2()

        else: 

            print("Do something sane.")

        print("What would you do next?")


def term():

    print('*The text on the screen says: "Press ENTER to continue"*')
    input(prompt)
    call("clear")
    print_term("Hello! Everything you have to do is to answer the question.")
    print_term(f"Tell me, {name}, if another one of the doors existed, which number would it be marked?")
    print_term("You have only one attempt.")

    answer = input(prompt)

    try:

        answer = int(answer)

    except ValueError:

        print_term("Learn how to type integers, motherfucker.")
        dead("The trapdoor under you was opened, you falled into the Jacque Fresco memories and have never found the way back.")

    if answer == 55 + 34:
        print_term("Excellent! You have a chance to save your sanity in that place.")
        # joking around, repair it tomorrow
        print("Press ENTER to exit the terminal...")
        input()
        return True

    else:
        print("You shouldn't pass your math classes.")
        dead("The trapdoor under you was opened, you falled into the Jacque Fresco memories and have never found the way back.")
