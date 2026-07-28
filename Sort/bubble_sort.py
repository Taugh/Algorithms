# bubble_sort.py
"""Use case and recommendation: Bubble sort is a simple sorting algorithm that is easy to understand and implement. 
It is suitable for small datasets or educational purposes to demonstrate sorting concepts. However, 
it has a time complexity of O(n^2) in the average and worst cases, making it inefficient for large datasets compared to more 
advanced algorithms like quicksort or mergesort. It is not stable by default but can be made stable with slight modifications."""

def bubble_sort(arr):

    n = len(arr)
    for i in range(n):
        # Track if any swaps were made in this pass
        swapped = False
        for j in range(0, n-i-1):
            # Compare adjacent elements
            if arr[j] > arr[j+1]:
                # Swap if they are in the wrong order
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        # If no swaps were made, the array is sorted
        if not swapped:
            break
    return arr


lst = [64, 34, 25, 12, 22, 11, 90]
sorted_lst = bubble_sort(lst)
print(sorted_lst)