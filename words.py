

def print_upper_words(words, letters):

    """ Takes a list of words and returns uppercase string of words that start
    with one of the letters """

    result = """ """
    for w in words:
        caps = w.upper()
        for l in letters:
            cl = l.upper()
            if caps.startswith(cl):
                result = result + f" \n {caps}"
            

    print(result)


print_upper_words(['dogs','water','horse'], ['d','f','H'])
# this should print "HELLO", "HEY", "YO", and "YES"

print_upper_words(["hello", "hey", "goodbye", "yo", "yes"],["h", "y"])