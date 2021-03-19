# Exercises 6.15

from turtle import *

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

def bewege(n,           # amount of disks to be moved
           von,         # stating position
           nach,        # end position
           ueber,       # support position
           ):
    """
    Solves the Problem of Hanoi

    Requirements: No smaller disks are distributed on the end/support position
    prints out a list of iterative movement commands, no return
    Paul Münch 19.March 2021
    """
    if n == 1:
        print("Lege eine Scheibe von ", von, " nach ", nach)
    else:
        bewege(n-1, von, ueber, nach)
        bewege(1, von, nach, ueber)
        bewege(n-1, ueber, nach, von)
# bewege(3, 1, 2, 3)

def create_tree(n=1):
    """
    Creates a tree in Logo

    :param n: Variant of the tree 1-3 (Integer)
    """

    if n == 1:
        def baum(x):
            if x < 5:
                return
            else:
                forward(x)
                left(45)
                baum(x/2)
                right(90)
                baum(x/2)
                left(45)
                back(x)
            return

    elif n == 2:
        def baum(x):
            if x < 3:
                return
            else:
                forward(x)
                left(25)
                baum(x*3/4)
                right(90)
                baum(x/2)
                left(65)
                back(x)
            return

    elif n == 3:
        def baum(x):
            if x < 3:
                return
            else:
                forward(x)
                left(90)
                baum(x * 2/3)
                right(180)
                baum(x * 2/3)
                left(90)
                back(x)
            return

    left(90)
    baum(100)
    hideturtle()
    input()
# create_tree(3)
