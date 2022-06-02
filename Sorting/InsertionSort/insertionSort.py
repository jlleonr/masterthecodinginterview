from typing import List

'''
Sort an array using the Insertion Sort algorithm
'''
def insertionSort(array: List[int]) -> None:

    for step in range(1, len(array)):
        key: int = array[step]
        j: int = step - 1

        # Compare key with each element on the left of it,
        # until an element smaller than it is found.
        # For descending order, change key<array[j] to key>array[j].
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j = j - 1

        # Place key at after the element just smaller than it.
        array[j + 1] = key


data: List[int] = [9, 5, 1, 4, 3]

insertionSort(data)
print('Sorted Array in Ascending Order:')
print(data)
