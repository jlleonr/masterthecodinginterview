from typing import List


'''
Sort an array using the Merge Sort algorithm
'''


def mergeSort(list: List[int]) -> List[int]:
    # 1. Store the length of the list
    list_length: int = len(list)

    # 2. List with length less than is already sorted
    if list_length == 1:
        return list

    # 3. Identify the list midpoint and partition the list into a left_partition and a right_partition
    mid_point: int = list_length // 2

    # 4. To ensure all partitions are broken down into their individual components,
    # the merge_sort function is called and a partitioned portion of the list is passed as a parameter
    left_partition: List[int]  = mergeSort(list[:mid_point])
    right_partition: List[int] = mergeSort(list[mid_point:])

    # 5. The merge_sort function returns a list composed of a sorted left and right partition.
    return merge(left_partition, right_partition)


# 6. takes in two lists and returns a sorted list made up of the content within the two lists
def merge(left: List[int], right: List[int]) -> List[int]:
    # 7. Initialize an empty list output that will be populated with sorted elements.
    # Initialize two variables i and j which are used pointers when iterating through the lists.
    output: List = []
    i: int = 0
    j: int = 0

    # 8. Executes the while loop if both pointers i and j are less than the length of the left and right lists
    while i < len(left) and j < len(right):
        # 9. Compare the elements at every position of both lists during each iteration
        if left[i] < right[j]:
            # output is populated with the lesser value
            output.append(left[i])
            # 10. Move pointer to the right
            i += 1
        else:
            output.append(right[j])
            j += 1
    # 11. The remnant elements are picked from the current pointer value to the end of the respective list
    output.extend(left[i:])
    output.extend(right[j:])

    return output


lst: List[int] = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
print(mergeSort(lst))