#!/usr/bin/python3

""" a method that determines if all the boxes can be opened """

def canUnlockAll(boxes):
    """ takes a list of a list """
    
    keys = [0]
    for key in keys:
        for boxkey in boxes[key]:
            if boxkey not in keys and boxkey < len(boxes):
                keys.append(boxkey)

    return len(keys) == len(boxes)
