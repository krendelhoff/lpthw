# close - closes the file. Like File -> Save.. in your editor
# read - Reads the contents of the file. You can assign the result to a variable.
# readline - Reads just one line of a text file.
# truncate = Empties the file. Wathc out if you care about the file.
# write('stuff') - writes "stuff" to the file
# seek(0) - move the read/write location to the beginning of the file

from sys import argv

#if len(argv) != 2:
#   print(f"Usage: python3 {argv[0]} <filename>")
#else:
#   script, filename = argv
#   txt = open(filename, "w")
#   print("That's the content of the file:\n" + txt.read())
#   print("Truncating!")
#   txt.truncate()
#   print("Printing the file again:\n" + txt.read())
#   txt.close()
# Failed code - file may be exactly writable or readable

script, filename = argv

print(f"We're going to erase {filename}")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

# You see here what we do not have assign the return value of input necessarily
input("?")

print("Opening the file...")
target = open(filename, 'w')
# open tries to be safe by making you explicitly say you want to write or read or append a file
# i think that if we do not use that parameter at all it will implicitly become "r"
# there are also "r+", "w+" and "a+" modes, and it open the file in both read and write and,
# depending on the character use, position the file in different ways.
# yeah, just doing open(filename) opens it in 'r' mode

print("Truncating the file. Goodbye!")
target.truncate()
# It's not necessary, but it will override character by character from the beginning

print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

#target.write(line1 + '\n' + line2 + '\n' + line3 + '\n')
# Another variant
target.write(f"{line1}\n{line2}\n{line3}\n")
#target.write('\n')
#target.write(line2)
#target.write('\n')
#target.write(line3)
#target.write('\n')

print("And finally, we close it.")
target.close()

target = open(filename, 'r')

print("That's the contents of the file now:\n" + target.read())

target.close()