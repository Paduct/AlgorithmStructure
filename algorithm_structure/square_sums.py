# coding: utf-8
# Copyright 2020

"""Sorting algorithm."""

from math import modf, sqrt
from typing import List


def square_sums(number: int) -> List[int]:
    """Return a sorted list."""
    array: List[int] = list(range(number, 0, -1))

    for cursor in range(1, number):
        index: int = cursor

        for _ in range(number ** 2):
            for num in range(index, number):
                if modf(sqrt(array[0] + array[num]))[0] == 0.0:
                    index += 1
                    array.insert(0, array.pop(num))

                    if index == number:
                        return array
                    break
            else:
                for idx in range(index - 1, 0, -1):
                    if modf(sqrt(array[0] + array[idx]))[0] == 0.0:
                        index = idx
                        break

        if index <= cursor:
            break

    array.clear()
    return array
