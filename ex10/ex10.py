# if you use """, you can put everything, even " again, until it meet """

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line"
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)
formatter = "meow\b{}"
# You see - w is drown
print(formatter.format("kitty"))
# You can also use ''' instead of """ - with this, you can use """ inside string
print('''
Meow
Meow2
Meow3
''')
