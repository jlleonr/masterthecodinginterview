from typing import List, Tuple
import unittest, sys

import Arrays.twoSum as twoSum

class Test_Arrays(unittest.TestCase):
    def test_twoSumBestCaseScenario(self):
        # Arrange
        lst: List[int] = [3, 2, 1, 4]
        target: int = 7

        # Act
        result: Tuple = twoSum.sumTwo(nums= lst, target= target)

        # Assert
        self.assertTupleEqual(result, (0, 3))

    def test_twoSumAnotherScenario(self):
        # Arrange
        lst: List[int] = [2, 8, 5, 12]
        target: int = 13

        # Act
        result: Tuple = twoSum.sumTwo(nums=lst, target=target)

        # Assert
        self.assertTupleEqual(result, (1, 2))

    def test_twoWorstCaseScenario(self):
        # Arrange
        lst: List[int] = []
        target: int = 5

        # Act
        result: Tuple = twoSum.sumTwo(nums=lst, target=target)

        # Assert
        self.assertEqual(result, None)

    def test_twoWorstEdgeCase(self):
        # Arrange
        lst: List[int] = [1, 5, 4, 8]
        target: int = 3

        # Act
        result: Tuple = twoSum.sumTwo(nums=lst, target=target)

        # Assert
        self.assertEqual(result, None)
