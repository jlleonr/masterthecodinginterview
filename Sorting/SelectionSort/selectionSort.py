from typing import List

'''
Sort a list using the Selection Sort algorithm
'''
def selectionSort(nums: List[int]) -> None:
    lengthOfNums: int = len(nums)

    for i in range(lengthOfNums - 1):

        # Smallest is the first element of outer iteration
        smallest: int = i

        # Search from outter iteration to the right
        for j in range(i, lengthOfNums - 1):

            # Select always the smallest element in the inner iteration
            if nums[smallest] > nums[j + 1]:
                smallest = j + 1

        # If element at inner iteration is smaller than outter iteration,
        # swap the element at outer iteration with the element at inner iteration
        if nums[i] > nums[smallest]:
            nums[i], nums[smallest] = nums[smallest], nums[i]




sortThis: List[int] = [99, 44, 6, 2, 1, 5, 63, 87, 283, 0]
# sortThis: List[int] = [99, 44, 6, 2]
selectionSort(sortThis)

print(sortThis)