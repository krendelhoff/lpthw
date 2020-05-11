print("Let's practice everything.")
print('You\'d need to know \'bout escapes with \\ that do:')
print('\n newlines and \t tabs.')

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the need of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there in none
"""

print("--------------")
print(poem)
print("--------------")


five = 10 - 2 + 3 - 6
print(f"This should be five: {five}")

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates
    # it looks like we can return a list, but not neccesarily list, you can do consequentive assignment f, s, t = func(lol)

start_point = 10000
beans, jars, crates = secret_formula(start_point)
# Intredasting

# remember that this is another way to format string
print("With a starting point of: {}".format(start_point))
# it's just like with an f"" string
print(f"We'd have {beans} beans, {jars} jars, and {crates} crates.")

start_point = start_point / 10

print("We can also do that this way:")
formula = secret_formula(start_point) # look, formula becomes a list, so it's the way to return a list
print(formula) # look, it's seem to be tuple
# this is an eary way to apply a list to a format string
print("We'd have {} beans, {} jars, and {} crates".format(*formula))
# we send a list to format and format will put values consequentively
# i don't know why now but we have send not just formula, but *formula
# WOW look - * operator unpacks a list or turple for you, so *formula replaces by three consequentive values
# but if function definition in parameters *args means the opposite - put all values that function get into the list(tuple)