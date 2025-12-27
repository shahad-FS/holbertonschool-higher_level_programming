#!/usr/bin/python3
"""Module for pascal_triangle function"""


def pascal_triangle(n):
    """Function that returns a list of lists of integers"""
    if n <= 0:
        return []
    triangle = []
    for number in range(n):
        row = [1] * (number + 1)
        for j in range(1, number):
            row[j] = triangle[number - 1][j - 1] + triangle[number - 1][j]
        triangle.append(row)
    return triangle
