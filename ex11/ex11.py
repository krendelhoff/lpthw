print("How old are you?", end=' ')
age = input()
print("How tall are you?", end=' ')
height = input()
print("How much do you weigh?", end=' ')
weight = input()
# we should use end parameter because print put \n character automatically, but we do not need this

print(f"So, you're {age} old, {height} tall and {weight} heavy.")
# Функция считывает строку данных, полученную с устройства ввода и возвращает её без заключительного перевода каретки. 
# That's what input() does

print(f"You can lift {input('How many kg can you lift? ')} kg")
# Another way to use input() - you can write prompt inside input() parameter
# input always return string, so if you want to use it as an int, you should use cast
num = int(input("Enter some arbitrary number: "))
print(f"You have entered {num}")
print(f"It's type is {type(num)}")
