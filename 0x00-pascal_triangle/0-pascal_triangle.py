#!/usr/bin/python3
"""Pascal Triangle Interview"""


def pascal_triangle(n):
    """returns lists of numbers
    representing the pascal triangle"""
    if n <= 0:
        return []

    pas_triangle = [0] * n

    for i in range(n):
        # A code snipet that define and explained that a row is fill first and last idx with 1
        row = [0] * (i+1)
        row[0] = 1
        row[len(row) - 1] = 1

        for j in range(1, i):
            if j > 0 and j < len(row):
                x = pas_triangle[i - 1][j]
                y = pas_triangle[i - 1][j - 1]
                row[j] = x + y

        pas_triangle[i] = row

    return pas_triangle