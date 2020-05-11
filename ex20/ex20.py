from sys import argv

script, input_file = argv
# unpacking

def print_all(f):
    print(f.read())

def rewind(f):
    f.seek(0)

def print_a_line(line_count, f):
    print(line_count, f.readline())

current_file = open(input_file)

print("First let's print the whole file:\n")

print_all(current_file)

print("Now let's rewind, kind of like a tape.")

# look, here you send object and it can be changed inside the function, maybe it's a pointer?
rewind(current_file)
# and after read() function the seek-position is at EOF

print("Let's print three lines:")

current_line = 1
print_a_line(current_line, current_file)

# current_line = current_line + 1
current_line += 1
print_a_line(current_line, current_file)

# current_line = current_line + 1
current_line += 1
print_a_line(current_line, current_file)
# readline() function also returns a string with the \n symbol, so you actually put \n twice, when use print()
# You can assign a string to a variable