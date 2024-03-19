#!/usr/bin/python3
"""
This script contains a method that calculates the fewest number of operations
needed to result in exactly n H characters in the file.
"""


def minOperations(n):
    """
    Args: The desired number of H characters.

    Returns: The minimum number of operations needed.
    """
    operations = 0
    min_op = 2
    while n > 1:
        while n % min_op == 0:
            operations += min_op
            n /= min_op
        min_op += 1
    return operations
