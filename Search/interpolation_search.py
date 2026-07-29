# interpolation_search.py
"""Use case and recommendation: Interpolation search is an improved variant of binary search for instances where the values 
in a sorted array are uniformly distributed. It works by estimating the position of the target value based on the values at 
the boundaries. It has a time complexity of O(log log n) for uniformly distributed data, but can degrade to O(n) in the worst 
case. It is more efficient than binary search for large, uniformly distributed datasets."""

def interpolation_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high and target >= arr[low] and target <= arr[high]:
        # Estimate the position of the target value
        pos = low + ((high - low) // (arr[high] - arr[low]) * (target - arr[low]))

        if arr[pos] == target:
            return pos
        elif arr[pos] < target:
            low = pos + 1
        else:
            high = pos - 1

    return -1

lst = [11, 12, 22, 33, 55, 90, 99]
print(interpolation_search(lst, 33))  # Output: 3
print(interpolation_search(lst, 100))  # Output: -1