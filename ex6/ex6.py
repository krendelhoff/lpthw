types_of_people = 10
# Enter variable into the string
x = f"There are {types_of_people} types of people."

binary = "binary"
do_not = "don't"
# 1 + 1 = 10
y = f"Those who know {binary} and those who {do_not}."

print(x)
print(y)


print(f"I said: {x}")
# Inside "" we can use '' and vise versa
print(f"I also said: '{y}'")

# It's actually funny
hilarious = False
# It's seems like we can hard code these {} and then format function finds that and enters our variable value
joke_evaluation = "Isn't that joke so funny?! {} ({})"
actually_hilarious = True

print(joke_evaluation.format(hilarious, actually_hilarious))

w = "This is the left side of..."
e = "a string with a right side."
# String concatenation
print(w + e)
