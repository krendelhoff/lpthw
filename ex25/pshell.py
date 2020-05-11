import ex25
sentence = "All good things come to those who wait."
words = ex25.break_words(sentence)
words # no effect
sorted_words = ex25.sort_words(words)
sorted_words
ex25.print_first_word(words)
ex25.print_last_word(words)
words
ex25.print_first_word(sorted_words)
ex25.print_last_word(sorted_words)
sorted_words
sorted_words = ex25.sort_sentence(sentence)
sorted_words
ex25.print_first_and_last(sentence)
ex25.print_first_and_last_sorted(sentence)
# use help() function in python shell bro
# from ex25 import * means you do not have to type ex25. every time
# None value means function didn't returned anything, and you are trying to assign it to some variable
# its value will be None