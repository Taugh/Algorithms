# selection_sort.py
"""Use case and recommendation: Selection sort is a simple comparison-based sorting algorithm that is easy to understand 
and implement. It is suitable for small datasets or educational purposes to demonstrate sorting concepts. However, 
it has a time complexity of O(n^2) in the average and worst cases, making it inefficient for large datasets compared to more 
advanced algorithms like quicksort or mergesort. It is not stable by default but can be made stable with slight modifications."""

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        # Assume the minimum is the first element of the unsorted part
        min_idx = i
        for j in range(i+1, n):
            # Update min_idx if a smaller element is found
            if arr[j] < arr[min_idx]:
                min_idx = j
        # Swap the found minimum element with the first element of the unsorted part
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

lst = [64, 34, 25, 12, 22, 11, 90]
sorted_lst = selection_sort(lst)
print(sorted_lst)