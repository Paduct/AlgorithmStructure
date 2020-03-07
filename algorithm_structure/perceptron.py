# coding: utf-8
# Copyright 2020

"""Neural network."""

from typing import List, Tuple


class Perceptron():

    """Perceptron implementation."""

    __slots__ = ("width", "height", "matrix")

    width: int
    height: int
    matrix: List[List[int]]

    def __init__(self, width: int, height: int):
        """Data structure creation."""
        self.width = width
        self.height = height
        self.matrix = [[0] * width for _ in range(height)]

    def training(self, model: Tuple[Tuple[int]]):
        """Adding new objects."""
        for row in range(self.height):
            for col in range(self.width):
                self.matrix[row][col] += model[row][col]

    def verify(self, model: Tuple[Tuple[int]], limit: int) -> bool:
        """Return the sign of the recognized object."""
        weight: int = 0

        for row in range(self.height):
            for col in range(self.width):
                weight += self.matrix[row][col] * model[row][col]

        return weight > limit
