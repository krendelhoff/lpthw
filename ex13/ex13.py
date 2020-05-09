from sys import argv, exit
# read the WYSS section for how to run this
if len(argv) == 5:
    script, first, second, third, fourth = argv
    # unpacking argv
else:
    print("Error")
    exit(1)
# Look, you can assign consequentively (script = argv[0], first = argv[1], second = argv[2] and so on)

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)
print("Your third variable is:", fourth)
print(f'You entered {input("Now, enter something! I am going to use it: ")}')
exit(0)