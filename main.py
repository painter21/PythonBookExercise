
# Exercises 6.15

def konkat(*args    # collection of strings
           ):
    """
    solves exercise 1: combines a list of strings

    Takes a sequence of strings and concatenate them. only works with strings, no catch for bad arguments.
    Returns a string
    Paul Münch, 19.March 2021
    """

    konkat_string = ""
    for string in args:
        konkat_string += string
    return konkat_string
# print(konkat('a', 'b', 'c'))

def verstecke(s,     # text (String)
              n=1   # number of added characters (Integer)
              ):
    """
    solves exercise 2: Encrypts a text with added characters

    Adds n random characters after each letter after uppercase the message. Returns a String
    Paul Münch, 19.March 2021
    """

    from random import randint

    s = s.upper()
    new_string = ""
    for char in s:
        new_string += char
        for i in range(n):
            new_string += chr(randint(65, 90))
    return new_string
# print(verstecke('Hallo', 15))

def wurzel(x,       # to be square rooted (Integer)
           n=10,     # runs (Integer)
           z=10      # so far calculated value (Float)
           ):
    """
    solves excercise 3: calculated the square root of x approximately

    uses the heron approximation to calculate the square root of x
    19.March 2021
    """
    if n == 1:
        return z
    else:
        return wurzel(x, n-1, 0.5*(z + x/z))
# print(wurzel(144))
