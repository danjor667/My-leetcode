#!/usr/bin/python3

def removeDuplicates(nums: list) -> int:
    """
    >>> nums = [1,1,1,2,2,3,3,4,5,6,7,7,]
    >>> unique = removeDuplicates(nums)
    >>> print(unique)
    7
    >>> print(nums[:unique])
    [1, 2, 3, 4, 5, 6, 7]
    """
    i = 0
    j = 1
    if nums and nums != []:
        count = 1
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                nums[i + 1] = nums[j]
                i += 1
                count += 1
        return count
    else:
        return 0
if __name__ == "__main__":
    import doctest
    doctest.testmod()

