# linear_search.py

def linear_search(arr, target):
    """
    Perform a linear search on the given array to find the target value.

    Parameters:
    arr (list): The list of elements to search through.
    target: The value to search for in the list.

    Returns:
    int: The index of the target value if found, otherwise -1.
    """
    index = 0
    found = False
    # Match the target value with each element in the array
    while index < len(arr) and not found:
        if arr[index] == target:
            found = True   
        else:
            index += 1
    # Return the index if found, otherwise return -1
    if found:
        return index
    else:
        return -1

lst = [12, 33, 11, 99, 22, 55, 90]
print(linear_search(lst, 22))  # Output: 4
print(linear_search(lst, 100))  # Output: -1