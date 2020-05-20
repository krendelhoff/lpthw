# comparisons return boolean expressions.
# result = 10 < (100 * 100) <= 10000  # True, the multiplication is evaluated once
# boolean chaining
# allowed = (h <= 10 < w <= 35 < l <= 40) or (h + w + l <= 80) - ok expression, returns boolean
# People generally don't choose Python to write fast code. The main advantages of Python are readability and simplicity. As the while
# loop requires 
# the introduction of extra variables, it takes more time for an iteration. Thus, the while loop is quite slow and not so popular.
# It resembles a conditional operator: using the while loop, we can execute a set of statements as long as the condition is true.
i = 0
while i <= 10:
    i = i + 1
    if i > 7:
        i = i + 2
print(i)