# shell_sort.py
"""Use case and recommendation: Shell sort is an in-place comparison-based sorting algorithm that generalizes insertion sort to allow 
the exchange of items that are far apart. It improves the efficiency of insertion sort for medium to large datasets. The time complexity
depends on the gap sequence used, but it is generally better than O(n^2) for large lists. """

def shell_sort(arr):
    n = len(arr)
    gap = n // 2  # Initialize the gap size

    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            # Perform a gapped insertion sort
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2  # Reduce the gap size for the next iteration
    return arr

lst = [64, 34, 25, 12, 22, 11, 90]
sorted_lst = shell_sort(lst)
print(sorted_lst)