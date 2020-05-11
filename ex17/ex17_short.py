from sys import argv
open(argv[2], 'w').write(open(argv[1], 'r').read()); print("", end='')
# One line, but don't know how to close file
# But we actually do not need it here
# Actually you can use ; too
# ohhh, if you are doing file this (do not assign file object to some variable) the file will be closed automatically