#!/usr/bin/python3


def median(nums1: list, nums2: list) -> float:
    """
    >>> nums1 = [1, 2, 3, 4]
    >>> nums2 = [6, 8, 10]
    >>> print(median(nums1, nums2))
    4.0
    >>> num1 = [2,4,6,8,]
    >>> nums2 = [3,5,7,10]
    >>> print(median(nums1, nums2))
    5.5
    """
    nums = nums1 + nums2
    nums.sort()
    n = len(nums) // 2
    if len(nums) % 2 == 1:
        return float(nums[n])
    else:
        return nums[n] + nums[n - 1] / 2
"""
O(m+n)(log(m+n))
note time complexity is greater than required O(log(m+n))
"""


if __name__ == "__main__":
    import doctest
    doctest.testmod()
