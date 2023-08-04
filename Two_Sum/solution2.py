#!/usr/bin/python3


def two_sum(nums: list, target: int) -> list:
    my_dict = {}
    for i in range(len(nums)):
        comp = target - nums[i]
        if comp in my_dict and my_dict[comp] != i:
            return [my_dict[comp], i]
        my_dict[nums[i]] = i
    return [-1, -1]
