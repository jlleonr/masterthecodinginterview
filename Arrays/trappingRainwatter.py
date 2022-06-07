"""Given an array that represent the height of towers with a
width of 1 block, calculate how much rain water can be trapped."""


from typing import List


def rainwaterTrapped(input: List[int]) -> int:
    """Find trapped water by using the following formula:
        trappedWater = min(maxLeftTower, MaxRIghtTower) - currentHeight"""

    length: int = len(input)

    if length < 1:
        return 0

    trappedWater: int = 0

    for i in range(length):
        maxLeft: int = 0
        maxRight: int = 0

        j: int = i-1
        while j >= 0:
            maxLeft = max(maxLeft, input[j])
            j -= 1

        j = i + 1
        while j < length:
            maxRight = max(maxRight, input[j])
            j += 1

        accumulatedWater: int = min(maxLeft, maxRight) - input[i]

        if accumulatedWater > 0:
            trappedWater += accumulatedWater

    return trappedWater


def trappedWaterOptimal(nums: List[int]) -> int:
    """Find trapped water by using two shifting pointers"""

    if len(nums) < 2:
        return 0

    trappedWater: int = 0
    maxLeft: int = 0
    maxRight: int = 0
    left: int = 0
    right: int = len(nums) - 1

    while left < right:
        if nums[left] < nums[right]:
            if nums[left] < maxLeft:
                trappedWater += maxLeft - nums[left]
                left += 1
            else:
                maxLeft = nums[left]
                left += 1
        else:
            if nums[right] < maxRight:
                trappedWater += maxRight - nums[right]
                right -= 1
            else:
                maxRight = nums[right]
                right -= 1

    return trappedWater


towers: List[int] = [0, 1, 0, 2, 1, 0, 3, 1, 0, 1, 2]
result: int = trappedWaterOptimal(towers)
print(result)
