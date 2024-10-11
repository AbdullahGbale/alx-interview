#!/usr/bin/python3
""" a method that determines if all the boxes can be opened """


def canUnlockAll(boxes):
    """Function that takes a list of a list and the
    contents of a list will unlock other lists
    """

    keys = [0]
    for key in keys:
        for boxKey in boxes[key]:
            if boxKey not in keys and boxKey < len(boxes):
                keys.append(boxKey)
    return len(keys) == len(boxes)  #check

# Remove whitespace
