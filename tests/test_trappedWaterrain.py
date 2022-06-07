"""Unit tests for trappingRainwater.py"""
from typing import List
import unittest
import Arrays.trappingRainwatter as trw


class TestTrappedRainwater(unittest.TestCase):
    def test_trappedWaterOptimal(self):
        # Arrange
        input: List[int] = [0, 1, 0, 2, 1, 0, 3, 1, 0, 1, 2]

        # Act
        result: int = trw.trappedWaterOptimal(input)

        # Assert
        self.assertEqual(result, 8)

    def test_trappedWaterOptimalEmptyArray(self):
        # Arrange
        input: List[int] = []

        # Act
        result: int = trw.trappedWaterOptimal(input)

        # Assert
        self.assertEqual(result, 0)

    def test_trappedWaterOptimalNoContainers(self):
        # Arrange
        input: List[int] = [1, 1, 1, 1, 1]

        # Act
        result: int = trw.trappedWaterOptimal(input)

        # Assert
        self.assertEqual(result, 0)
