from typing import List


'''
You are given an input array with numbers that represent
the height of towers. Find the towers that will trap the most
water and return the area of trapped water.
'''


def getArea(nums: List[int]) -> int:    # T = O(n**2), S =O(1)

    if len(nums) < 2:
        return 0

    area: int = 0
    numsLength: int = len(nums)

    for i in range(numsLength):
        for j in range(i + 1, numsLength):

            # Area = length * width
            #      = min(height1, height2) * (index2 - index1)
            tempArea: int = min(nums[i], nums[j]) * (j - i)

            if tempArea > area:
                area = tempArea

    return area


'''
Optimise by shifting oposite pointers.
If a < b, move a pointer to the right.
Else move b pointer to the left.
'''


def getAreaOptimal(nums: List[int]) -> int:  # T = O(n), S = O(1)

    # If array is empty or has a single element
    #  return None
    if len(nums) < 2:
        return 0

    # Declare pointers to the first and last elements
    left: int = 0
    right: int = len(nums) - 1
    maxArea: int = 0
    tempArea: int = 0

    maxArea: int = min(nums[left], nums[right]) * (right - left)

    while left < right:

        if nums[left] <= nums[right]:
            left += 1
        else:
            right -= 1

        tempArea = min(nums[left], nums[right]) * (right - left)

        if tempArea > maxArea:
            maxArea = tempArea

    return maxArea
