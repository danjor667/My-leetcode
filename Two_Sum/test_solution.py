#!/usr/bin/python3
"""
testing
"""
import unittest
from solution import two_sum


class Test_two_sum(unittest.TestCase):
    """
    DOC
    '"""
    def test_solution_exist(self):
        self.assertEqual(two_sum([0, 3, 6, 8, 4, 7], 9), [1, 2])
        self.assertEqual(two_sum([5, 0, 6, 8, 10, 7], 9), [-1, -1])

    def test_solution_not_exist(self):
        self.assertNotEqual(two_sum([3, 5, 9], 12), [-1, -1])


if __name__ == "__main__":
    unittest.main()
