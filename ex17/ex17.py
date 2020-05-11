from sys import argv
from os.path import exists

# handy way to write a string into a file echo "This is a test file" > test.txt
# You already knew about it.
# echo "" > test2 - truncate the file

script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")

# we could do these two on one line, how?
# indata = open(from_file).read()
in_file = open(from_file)
indata = in_file.read()
# Look how you can do man - open returns object so you can use is that way

print(f"The input file is {len(indata)} bytes long")

print(f"Does the output file exists? {exists(to_file)}")
#exists function return us True if file is in current working directory
#print("Ready, hit RETURN to continue, CTRL-C to abort.")
#input()
# just waiting to input just something - \n in that case

out_file = open(to_file, 'w')
out_file.write(indata)
# indata is content of all the file, so we can write all file
# if you open with the "w" option, file will be created if it is not exists in current directory
# cat is used to "con*cat*enate" files together

print("Alright, all done.")

out_file.close()
in_file.close()