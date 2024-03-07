#!/usr/bin/python3
"""Pascal Triangle Interview"""


def pascal_triangle(n):
    """returns lists of numbers
    representing the pascal triangle"""
    if n <= 0:
        return []

    pas_triangle = [1]

    for i in range(1, n):
        row = [1]
        prev_row = pas_triangle[1, i]

        for j in range(1, i):
        # Calculate each element of the row based on the previous row
            row.append(prev_row[j - 1] + prev_row[j])
        row.append(row)

    return pas_triangle
