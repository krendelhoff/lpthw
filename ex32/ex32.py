# if number is in range, you can use that notation 0 < x < 10, or x in range(1, 10)
x = 5
if 0 < x < 10:
    #print(x)
    5
# making a lists here
the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this first kind of for-loop goes through a list
for number in the_count:
    print(f"This is count {number}")

# same as above
for fruit in fruits:
    print(f"A fruit of type: {fruit}")
# we iterate over fruits
# also we can go through mixed lists too
# notice we have to use {} we don't know what's in it
for i in change:
    print(f"I got {i}")

# we can also build lists, first start with an empty one
elements = []
elements = list() # another way to create an emply list

# then use the range function to do 0 to 5 counts
# range function returns list [0, 1, 2, 3, 4, 5] and for iterates over it. range return a list
# you can put every list besides range here
# for i in range(0, 6):
#    print(f"Adding {i} to the list.")
#    # append is a function that lists understand
#    elements.append(i)
elements = range(6) # just returns a list, so we do iterate or check with "in" using the list, it can be every list
# NO. range returns tuple. fuck, not even a tuple. a range. but it is a list. just a list. of consequentive values

# now we can print them out too
for i in elements:
    # variable i defines for the for-loop when it starts
    print(f"Element was: {i}")

# pop(i) function pop's i-th element and returns it
# list.sort() function sorts it. sorted(list) function returns sorted list, do not affect the initial list
# string.split(' ') turn a string into a list of words

list2d = [[1, 2, 3], [4, 5, 6]]
# list of lists