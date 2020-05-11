from sys import exit
print("Well, hello.")
print("Here I am gonna teach you how to live.")
print("Do you want to get that knowledge?")
prompt = "> "
while True:
    answer = input(prompt)
    if answer.lower() in ['y', "yes"]:
        print("Excellent.")
        print("But why do you think you deserve it?")
        print("Tell me why.")
        why = input(prompt)
        print("Nice. I accept this.")
        answered, answered1, answered2, answered3 = False, False, False, False
        for i in range(4):
            print("What do you want to find out?")
            if not(answered1):
                print("1. Who am I?")
            if not(answered2):
                print("2. Why am I here?")
            if not(answered3):
                print("3. Why me?")
            if answered:
                print("4. Why should I know this?")
            answer = input(prompt)

            if answer == '1':
                print("My name is Jacque Fresco.")
                answered1 = True
        
            elif answer == '2':
                print("You are here because you should listen to that story. The main thesis is that rich people are dumb")
                print("One day, the very rich man asked me.")
                print("\"Jacque, if you are so smart, why aren't you rich, as me?\" (c)")
                print("And then I said: \"Shut the fuck up. \"")
                answered, answered2 = True, True

            elif answer == '3':
                print("I knew your mother, son.")
                answered3 = True
            
            elif answer == '4':
                print("Bababa with bebebe.")
                print("Bye.")

        break

    elif answer.lower() in ['n', "no"]:
        print("Well, that's your choice. Continue your pointless life.")
        break
    
    else:
        print("You have only two options: agree or disagree. I determine your capabilities here. And you do not have a way back.")