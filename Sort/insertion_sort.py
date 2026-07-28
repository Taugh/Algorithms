# insertion_sort.py
""" Use case and recommendation: Insertion sort is efficient for small datasets or nearly sorted data. 
It is stable and works well for linked lists. However, it has a time complexity of O(n^2) in the average and worst cases, 
making it less suitable for large datasets compared to more advanced algorithms like quicksort or mergesort. """

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

lst = [64, 34, 25, 12, 22, 11, 90]
sorted_lst = insertion_sort(lst)
print(sorted_lst)