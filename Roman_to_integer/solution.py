#!/usr/bin/python3


def roman_to_int(s: str) -> int:
    """
    return the integer equivilent from a quaranty valid string
    representation of a roman numeral
    """
    my_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    value = 0
    for i in range(len(s) - 1):
        if my_dict.get(s[i + 1]) > my_dict.get(s[i]):
            value -= my_dict.get(s[i])
        else:
            value += my_dict.get(s[i])
    value += my_dict.get(s[-1])
    return value
