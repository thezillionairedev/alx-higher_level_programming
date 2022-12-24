#!/usr/bin/python3

def add_integer(a, b=98):
    """Returns the additiion of a and b

    Float are casted to integers first
    Otherwise raise a TypeError"""

    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an interger")
    if((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an interger")
    return (int(a) + int(b))
