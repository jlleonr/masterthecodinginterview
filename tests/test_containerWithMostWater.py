from typing import List
import unittest

import Arrays.containerWithMostWater as containerWMW


class TestContainerWithMostWater(unittest.TestCase):
    def testgetAreaBestCaseScenario(self):
        # Arrange
        input: List[int] = [1, 8, 6, 2, 9, 4]

        # Act
        result: int = containerWMW.getArea(nums=input)

        # Assert
        self.assertEqual(result, 24)

    def testgetAreaBestCaseScenario2(self):
        # Arrange
        input: List[int] = [3, 5, 9, 6]

        # Act
        result: int = containerWMW.getArea(nums=input)

        # Assert
        self.assertEqual(result, 10)

    def testgetAreaEmptyListScenario(self):
        # Arrange
        input: List[int] = []

        # Act
        result: int = containerWMW.getArea(nums=input)

        # Assert
        self.assertEqual(result, 0)

    def testgetAreaSingleElementScenario(self):
        # Arrange
        input: List[int] = [3]

        # Act
        result: int = containerWMW.getArea(nums=input)

        # Assert
        self.assertEqual(result, 0)

    def testgetAreaOptimalBestCaseScenario(self):
        # Arrange
        input: List[int] = [1, 8, 6, 2, 9, 4]

        # Act
        result: int = containerWMW.getAreaOptimal(nums=input)

        # Assert
        self.assertEqual(result, 24)

    def testgetAreaOptimalBestCaseScenario2(self):
        # Arrange
        input: List[int] = [3, 5, 9, 6]

        # Act
        result: int = containerWMW.getAreaOptimal(nums=input)

        # Assert
        self.assertEqual(result, 10)

    def testgetAreaOptimalEmptyListScenario(self):
        # Arrange
        input: List[int] = []

        # Act
        result: int = containerWMW.getAreaOptimal(nums=input)

        # Assert
        self.assertEqual(result, 0)

    def testgetAreaOptimalSingleElementScenario(self):
        # Arrange
        input: List[int] = [3]

        # Act
        result: int = containerWMW.getAreaOptimal(nums=input)

        # Assert
        self.assertEqual(result, 0)
