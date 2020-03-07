# coding: utf-8
# Copyright 2020

"""Testing module."""

from math import modf, sqrt
from typing import List, Set
from unittest import TestCase, TestLoader, TestSuite

from perceptron import Perceptron
from square_sums import square_sums


class Tests(TestCase):

    """Collection of tests for modules."""

    def test_perceptron(self):
        """Structure testing."""
        limit: int = 12
        perceptron: Perceptron = Perceptron(5, 5)

        perceptron.training(((1, 0, 1, 0, 0),
                             (1, 0, 1, 0, 0),
                             (1, 1, 1, 0, 0),
                             (0, 0, 1, 0, 0),
                             (0, 0, 1, 0, 0)))
        perceptron.training(((0, 1, 0, 1, 0),
                             (0, 1, 0, 1, 0),
                             (0, 1, 1, 1, 0),
                             (0, 0, 0, 1, 0),
                             (0, 0, 0, 1, 0)))
        perceptron.training(((0, 0, 1, 0, 1),
                             (0, 0, 1, 0, 1),
                             (0, 0, 1, 1, 1),
                             (0, 0, 0, 0, 1),
                             (0, 0, 0, 0, 1)))

        self.assertTrue(perceptron.verify(((0, 1, 0, 1, 0),
                                           (0, 1, 0, 1, 0),
                                           (0, 1, 1, 1, 0),
                                           (0, 0, 0, 1, 0),
                                           (0, 0, 0, 1, 0)), limit))
        self.assertFalse(perceptron.verify(((0, 1, 0, 1, 0),
                                            (0, 1, 0, 1, 0),
                                            (0, 1, 0, 1, 0),
                                            (0, 0, 0, 1, 0),
                                            (0, 0, 0, 1, 0)), limit))

    def test_square_sums(self):
        """Algorithm testing."""
        negative_numbers: Set[int] = set(range(25)) - {15, 16, 17, 23}

        for number in range(100):
            array: List[int] = square_sums(number)

            if array:
                self.assertNotIn(number, negative_numbers)
                self.assertEqual(len(array), len(set(array)))

                for index in range(1, number):
                    self.assertEqual(
                        modf(sqrt(array[index - 1] + array[index]))[0], 0.0
                    )
            else:
                self.assertIn(number, negative_numbers)


def suite() -> TestSuite:
    """Return a test suite for execution."""
    tests: TestSuite = TestSuite()
    loader: TestLoader = TestLoader()
    tests.addTest(loader.loadTestsFromTestCase(Tests))
    return tests
