# Quick Sort
- Logic
   - Divide and conquer.
   1. An array is divided into subarrays by selecting a pivot element (element selected from the array).

    2. While dividing the array, the pivot element should be positioned in such a way that elements less than pivot are kept on the left side and elements greater than pivot are on the right side of the pivot.
    3. The left and right subarrays are also divided using the same approach. This process continues until each subarray contains a single element.
    4. At this point, elements are already sorted. Finally, elements are combined to form a sorted array.
- Time Complexity
    - O(n Log(n))

- Space Complexity
    - O(n)