# summary: for-loop can only iterate over collection of things
# a while loop can do any kind of iteration you want
# ordinal == ordered, 1st; cardinal == cards at random, 0.
# at 1 - cardinal number, the real index, the first - ordinal number, real first
# remember it *(A + i) <===> A[i]
# zero means zero shift relative to the start of list
animals = ['bear', 'python3.6', 'peacock', 'kangaroo', 'whale', 'platypus']
print(animals)
print("The animal at 1:", animals[1])
print("The third animal:", animals[2])
print("The first animal:", animals[0])
print("The animal at 3:", animals[3])
print("The fifth animal:", animals[4])
print("The animal at 2:", animals[2])
print("The sixth animal:", animals[5])
print("The animal at 4:", animals[4])
# answer the first question - we started to count not from zero, it's ordinal number
# You can read a guy called Dijkstra about this subject(cardinal and ordinal numbers i suppose)
# why it starts from 0, not 1