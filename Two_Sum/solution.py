#!/usr/bin/python3

def two_sum(nums: list, target: int) -> list:
    for i in range(len(nums)):
        for j in range(1, len(nums)):
            if nums[i] != nums[j] and nums[i] + nums[j] == target:
                return [i, j]
    return [-1, -1]
