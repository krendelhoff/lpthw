from sys import argv
import pathlib

# That thing is really called unpacking
script, user_name, liar = argv
prompt = f'{pathlib.Path().absolute()}> '
# It's the example of shell prompt and it show you the power of python in system scripts
# because all you need is API with the operating system and that's all
# and that also show you that everything can be written in either language
# EVERYTHING
# you only need API(it's written with assembly or what ever)

print(f"Hi {user_name}, I'm the {script} script.")
print(f"You said you are a {liar}, huh?")
print("I'd like to ask you a few questions.")
print(f"Do you like me {user_name}?")
likes = input(prompt)

print(f"Where do you live, {user_name}?")
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

# As you can see, you also can use """-string as formatted
print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer} computer. Nice.
""")