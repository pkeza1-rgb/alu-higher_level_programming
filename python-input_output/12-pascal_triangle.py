#!/usr/bin/python3
"""Module that defines pascal_triangle."""


def pascal_triangle(n):
    """Return a list of lists representing Pascal's Triangle."""
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        previous = triangle[-1]
        row = [1]

        for j in range(1, i):
            row.append(previous[j - 1] + previous[j])

        row.append(1)
        triangle.append(row)

    return triangle
