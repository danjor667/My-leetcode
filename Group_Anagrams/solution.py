#!/usr/bin/python3

def groupAnagrams(strs: list)-> list:
    """
    >>> st = ["eat","tea","tan","ate","nat","bat"]
    >>> print(groupAnagrams(st))
    [["bat"],["nat","tan"],["ate","eat","tea"]]

    """
    my_dict = {}
    result = []
    for word in strs:
        key = [char for char in word]
        key = tuple(sorted(key))
        if key in my_dict:
            my_dict[key].append(word)
        else:
            my_dict[key] = [word]
    for value in my_dict.values():
        result.append(value)
    return result

if __name__ == "__main__":
    import doctest
    doctest.testmod()
