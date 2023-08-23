#!/usr/bin/python3


def lengthOfLastWord(s:str) -> int:
    """
    >>> s = "testing the solution"
    >>> lengthOfLastWord(s)
    8
    """
    return len(s.split()[-1])
if __name__ == "__main__":
    import doctest
    doctest.testmod()
