# merge_sort.py
"""Use case and recommendation: Merge sort is a divide-and-conquer algorithm that is efficient for large datasets. 
It has a time complexity of O(n log n) in the average and worst cases, making it suitable for sorting large lists.
It is stable and works well for linked lists. However, it requires additional memory for the temporary arrays used during 
the merge process. """

def merge_sort(arr):
    # Base case: If the array has one or zero elements, it is already sorted
    if len(arr) > 1:
        mid = len(arr) // 2  # Split the array into two halves
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)  # Sort the first half
        merge_sort(R)  # Sort the second half

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # if there are any remaining elements in L copy them over
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        # if there are any remaining elements in R copy them over
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr

lst = [64, 34, 25, 12, 22, 11, 90]
sorted_lst = merge_sort(lst)
print(sorted_lst)