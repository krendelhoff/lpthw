# very useful function type(), you can also use it as type(object) == str
# when you create a list using the list() object you can put there an iterable object.
# so if you put a list("danger") you have putted an iterable object and list will be
# ['d','a','n','g','e','r'], iterable object is object you can iterate through, one by one.
# range is iterable, generator too., lists, tuples, dicts, sets.
# So, the list function creates a list containing each element from the given iterable object such as a string.
# You can use square brackets or invoke the list functions depending on your task.
# Sometimes you need to know how many elements are there in a list. There is a built-in function called len that 
# can be applied to any iterable object, and it returns simply the length of that object
# you also can write print([1, 2, 3]); print(list()); print([])
# you can use [n] notation with every sequence in python; Positionally ordered collections of elements are usually called sequences;
# string, lists, tuples
# every sequence is iterable
# you cannot modify the string via the [n] notation
# . Strings, unlike lists, are immutable, so you can't modify their contents with indexes: pet = "cat"; pet[0] = "b" is wrong
while True:
    try:
        word = input()
        if word == "exit":
            break
    # you can prevent interrupting the program
    # if you type just except: then every exception will be handled here(except the SyntaxError)
    except KeyboardInterrupt:
        print()
        print("Don't do this.")
# Rules of modulus operations
# Divide the number by itself
print(4 % 4)     # 0
# At least one number is a float
print(11 % 6.0)  # 5.0
# The first number is less than the divisor
print(55 % 77)   # 55
# With negative numbers, it preserves the divisor sign
print(-7 % 3)    # 2
print(7 % -3)    # -2 

# You can break line inside the parentheses
count = (5 
        + 5
        - 20
        + 39492
        / 2)
print(count)
# The operators or and and return one of 
# their operands, not necessarily of the boolean type. Nonetheless, not always returns a boolean value.
a = True
b = False
c = a and not b
print(a and (not c or b))
# Короче, он возвращает значение которое прочитал последнее в булевом выражении.
# If the most suitable variable name is some Python keyword, add an underscore to the end of it.
# class_ = type(var)
# str = 'Hello!'  # no, because in the further code you can't use str type as it's overridden
# for key, value in counts.items(): - returns a list of tuples with key and value and you assign consequentively
# sorted() function sorts any iterable object and returns object, do not affect the inital object
# so you can sort it - for key, value in sorted(counts.items()):
# sorted also get a comparator function as a parameter as qsort in Clang
# so you can pass a function names as arguments
# for key, value in sorted(counts.items, key=comp, reverse=True)
# for key, value in sorted(counts.items, key=lambda item: item[1], reverse=True)
# there is builtin method list.sort()