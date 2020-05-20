from time import sleep
from subprocess import call
from printlib import prints, dead
from main_room import main_room
from header import name, prompt
from inv import take
# remember it, you can rename modules



def main():

    call("clear")

    prints("Hello, boy!", 2)
    prints("Why did you come here?...", 2)
    prints("There is nothing interesting you can find here.", 2)
    prints("But...there is actually no way back. That's why I am still here.", 2)

    print("Tell me your name. I have to call you somehow.")

    name = input(prompt)

    prints(f"Hmm, intredasting.", 2)
    prints(f"My name is Jacque. Jacque Fresco. Well, {name}, we have a plenty of time to talk around.", 2)
    prints("To be precise, the eternity.", 2)
    prints("But at first, I have to offer you something.", 2)
    prints("Go inside that door.", 2)
    prints("Do you wanna see what's there?", 2)
    prints("You will never have such chance anymore.", 2)

    answer = input(prompt).lower()

    if answer in ['yes', 'y']:
        prints("Excellent. Take this.", 2)
        take("tesseract")
        main_room()

    elif answer in ['no', 'n']:
        dead("Jacque talked to you about resource-oriented economics for eternity and you become mad.")

main()