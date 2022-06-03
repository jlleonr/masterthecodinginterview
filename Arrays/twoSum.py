from typing import List, Tuple


'''
Given an array of integers, return the indices of the two numbers
that add up to a given target
'''
def sumTwo(nums: List[int], target: int) -> Tuple[int, int]:
# Check if the complement of the value exist in a hash set
# If the value does not exist, add the complement to the set
# Add the value as a key to a dictionary and the index as the value
# If we find the comp in the set, return the current index and the
# value of dict[target - value] which will give the second index

    if len(nums) < 2:
        return None

    indexes: dict = dict()

    for index, value in enumerate(nums):
        if value in indexes:
            return (indexes[value], index)

        indexes[target - value] = index

    return None

testNums: List[int] = [3, 2, 1, 4]
testTarget: int = 7

print(sumTwo(nums= testNums, target= testTarget))
