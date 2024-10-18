#!/usr/bin/python3
''' script that implements a copyAll - paste task
'''


def minOperations(n):
    ''' Method that computes min. no. of
    operations for a task.

    Args:
        n: input
        operations: list to save operations
    Return: sum of operations
    '''
    if n < 2:
        return 0
    operations = []
    i = 1
    while i != 1:
        i += 1
        if n % i == 0:
            while n % i == 0:
                n /= i
                operations.append(i)
                return sum(operations)
