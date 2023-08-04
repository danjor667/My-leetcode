#!/usr/bin/python3

import unittest
from solution import roman_to_int


class Test_roman(unittest.TestCase):
    def test_romant_to_int(self):
        self.assertEqual(roman_to_int("XIX"), 19)
    """
    we dont have to test for invalid string input
    as it is garanty that the string will always be a
    valid representation of a roman numeral
    """
if __name__ == "__main__":
    unittest.main()
