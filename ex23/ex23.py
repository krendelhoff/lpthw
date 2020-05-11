import sys
script, input_encoding, error = sys.argv
# look, if you specify from sys import argv, you do not have to use sys. notation

def main(language_file, encoding, errors):
    line = language_file.readline()

    # we are checking if there is a line, so one day it will return EOF and that condition won't execute
    # readline return an empty string if there is nothing to read anymore
    if line:
        print_line(line, encoding, errors)
        return main(language_file, encoding, error)
        # recursion

def print_line(line, encoding, errors):
    # strip removes leading and trailing whitespaces and \n
    next_lang = line.strip()
    raw_bytes = next_lang.encode(encoding, errors=errors)
    cooked_string = raw_bytes.decode(encoding, errors=errors)
    # encode and decode are library functions with named parameters errors

    print(raw_bytes, "<===>", cooked_string)

# i think if we put the file encoded in another codec it will be error because we explicitly said that encoding is utf-8
languages = open("languages.txt", encoding="utf-8")
# here we break the string into bytes which are encoded by hex values
# english character becomes english again, but some foreign is the hex code

main(languages, input_encoding, error)
languages.close()
# LaTeX also can be used for programming languages, not just maths
# study and use recursion bro

#0bhhhhhhh is a notation for a binary number, where hhhhhhhh is binary number
#if you type hex number in the python shell, it will be converted to decimal, so as binary or octal(not sure)
#ord('Z') tells you the encodement code of the character
#chr(90) returns you a character encoded by 90
#char low level conversion a = chr(ord('Z') - ord('A') + ord('a')) yields z
# b'' is byte string, that numerical values converts to the real characters
# in python, string - in utf-8 encoded sequence of characters for displaying or working with text
# if you have raw bytes(just the numerical values) you must use decode() to get the string
# mnemonic rule DBES - decode bytes encode strings.
# if we do errors=strict, then there will be error if it can't encode, but replace option avoid this