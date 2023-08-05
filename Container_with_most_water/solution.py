#!/usr/bin/python3


def max_area(height: list) -> int:
    """
    >>> y = [1,8,6,2,5,4,8,3,7]
    >>> max_area(y)
    49
    """
    area = 0
    i = 0
    j = len(height) - 1
    while i < j:
        x = j - i
        y = min(height[i], height[j])
        new_area = x * y
        area = max(area,new_area)
        if height[i] >= height[j]:
            j -= 1
        else:
            i += 1
    return area
if __name__ == "__main__":
    import doctest
    doctest.testmod()
