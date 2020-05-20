# Rules for If-statement
# 1. Every if-statement must have an else.
# 2. If this else should never run because it doenn't make sense, then you must\
# use a die function in the eelse that prints out an error message and dies, just like you did in the last exercise
# This will find MANY errors.
# 3. Never nest if-statements more that two deep and always try to do them one deep.
# 4. Treat if-statements like paragraphs, where each if-elif-else grouping is like a set of sentences. Put blank lines before and after.
# 5. You Boolean tests should be simple. If they are complex, move their calculations to variables earlier in your function
# and use a good name for the variable
# opt: use blank lines more freely, python is ok with that and code become more readable. Always do comments. Always.
# If you follow that rules, you will start to write code better than most programmers.
# Rules for Loops
# 1. Use a while-loop only to loop forever, and that means probably never(!). This only applies to Python; other languages are
# different.
# 2. Use a for-loop for all other kinds of looping, esfecially if there is a fixed or limited of things to loop over.(and also
# if there is an object to iterate through)
# Tips for debugging
# 1. Do not use a "debugger". A debugger is like doing a full-body scan on a sick person. You do not get any specific useful
# information, and you find a whole lot of information that doesn't help and is just confusing.
# 2. The best way to debug a program is to use print to print out the values of variables at points in the program to see
# where they go wrong.
# 3. Make sure parts of your program work as you work on them. Do not write massive files of code before you try to run them.
# Code a little, run a little, fix a little. (important!)
str1 = "ls              -lah"
print(str1)
print(str1.split(" "))
