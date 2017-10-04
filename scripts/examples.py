"""Kabu Ihub Python Programming"""
from collections import OrderedDict


def longest(string):
    """
    print the longest sequence of characters in a string
    eg:
        ```
            >>> longest('aabbbbbcc')
            >>> 5
        ```

    :param string:
    :return: integer
    """
    chars = OrderedDict()  # order matters
    for i, char in enumerate(string):  # iterate through the string
        if not string[i] in chars.keys():  # check if string is in the chars dictionary
            chars.update({string[i]: 1})

        else:  # get the previous number of occurrences and increment by one
            total = chars.get(string[i]) + 1
            chars.update({string[i]: total})  # save the new value

    largest = None  # a variable that will hold the character with largest occurrences

    for item in chars.items():  # loop over the stored characters with there occurrences
        if largest is None:
            largest = item[0], item[1]

        else:
            if item[1] > largest[1]:
                largest = item[0], item[1]

    return largest[1]
