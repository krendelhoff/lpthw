def break_words(stuff):
    """This function will break up words for us.""" # it's just a string. Nothing would happen. It's like 2 + 2; in C
    words = stuff.split(' ')
    return words

def sort_words(words):
    """Sort the words."""
    return sorted(words)

def print_first_word(words):
    """Prints the first word after popping it off.""" # IT'S NOT JUST A STRING - it's documentation comments
    word = words.pop(0) # stack func, seems like removing 0 element and return it
    print(word)

def print_last_word(words):
    """Print the last word after popping it off."""
    word = words.pop(-1) # means len(words) - 1
    print(word)

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)
