from sys import argv

# script, filename = argv
filename = input("Enter the name of the file\n> ")
# It seems like we do not have to necessarily specify the "r", "w" or "a" option
txt = open(filename)

# We print the name of the file
print(f"Here's your file {filename}:")
# txt is the file object. Methon read() convert it to the string
print(txt.read(), end='')
txt.close()

# Here you see clearly that you can interact with the system and write system scripts
# print("Type the filename again:")
# Asking for a filename after the prompt
# file_again = input("> ")

# Doing exactly the same
# txt_again = open(file_again)

# print(txt_again.read())
# txt_again.close()