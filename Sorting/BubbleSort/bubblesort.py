from typing import List

'''
Sort an array using the Bubble Sort algorithm
'''
def bubbleSort(nums: List[int]) -> None:

    lstLength: int = len(nums)

    for i in range(lstLength - 1):
        for j in range(lstLength - 1):
            if nums[j] > nums[j + 1]:
                nums[j + 1], nums[j] = nums[j], nums[j + 1]

sortThis: List[int] = [99, 44, 6, 2, 1, 5, 63, 87, 283, 0]
bubbleSort(sortThis)

print(sortThis)