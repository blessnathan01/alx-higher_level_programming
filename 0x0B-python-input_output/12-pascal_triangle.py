#!/usr/bin/python3
"""
    12-pascal_triangle: pascal_triangle()
"""


def pascal_triangle(n):
    """
        returns a list of lists of integers
        Args:
            n (int): number of lists and digits
        Returns: list of lists
    """
    t_row = [1]
    tmp_l = [0]
    pasTri = []

    if n <= 0:
        return pasTri

    for i in range(n):
        pasTri.append(t_row)
        t_row = [l+r for l, r in zip(t_row + tmp_l, tmp_l + t_row)]
    return pasTri
