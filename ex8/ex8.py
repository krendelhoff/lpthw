# create a string with 4 formatters
formatter = "{} {} {} {}"

# put 1, 2, 3, 4 to their format places
print(formatter.format(1, 2, 3, 4))
# analoguous
print(formatter.format("one", "two", "three", "four"))
# author also show us that we can put any data type we want, including boolean
print(formatter.format(True, False, False, True))
# format function just return a string - it has no effect on the calling string. so we can put it to put in, why not? 
print(formatter.format(formatter, formatter, formatter, formatter))
# here you can find out that you can actually do random using of \n, but don't break the "" and that will be ok
# with the experience you will found out how you can play with that. If you not sure, use the \ character
# so you see, you can do random \n formatting inside function argument
print(formatter.format(
    "Try your",\
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
))