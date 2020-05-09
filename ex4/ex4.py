# Amount of cars
cars = 100
# How much people can car handle
space_in_a_car = 4
# Amout of drivers
drivers = 30
# Amount of passengers
passengers = 90
# If there are 100 cars and only 30 drivers, 100 - 30 cars will be not driven
cars_not_driven = cars - drivers
# Amount of drivers is the same as the amout of cars, because it's bijection
cars_driven = drivers
# Each car can handle 4 people, so 30*4 is the number of all people which can be handled
carpool_capacity = cars_driven * space_in_a_car
# We have to put this number of people in each car(in order to put equal quantity to each car)
average_passengers_per_car = passengers / cars_driven


print("There are", cars, "cars avaliable.")
print("There are only", drivers, "drivers avaliable.")
print("There will be", cars_not_driven, "emply cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We heed to put about", average_passengers_per_car, "in each car.")
