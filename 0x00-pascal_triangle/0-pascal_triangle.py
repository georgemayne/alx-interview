#!/usr/bin/python3
"""Pascal Triangle Interview"""


def pascal_triangle(n):
    """returns lists of numbers
    representing the pascal triangle"""
    if n <= 0:
        return []

    pas_triangle = []
    if n > 0:
        for i in range(1, n + 1):
            row = []
            C = 1
            for j in range(1, i + 1):
                row.append(C)
                C = C * (i - j) // j
            pas_triangle.append(row)
    return pas_triangle
