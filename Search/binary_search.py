# binary_search.py
"""Use case and recommendation: Binary search is an efficient algorithm for finding an item from a sorted list of items. 
It works by repeatedly dividing in half the portion of the list that could contain the item, until you've narrowed down 
the possible locations to just one. It has a time complexity of O(log n), making it much faster than linear search for 
large datasets. However, it requires the list to be sorted beforehand."""

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

lst = [11, 12, 22, 33, 55, 90, 99]
print(binary_search(lst, 22))  # Output: 2
print(binary_search(lst, 100))  # Output: -1