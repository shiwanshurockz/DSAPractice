import sys
def partition(arr, l, h):
    i = l
    j = h
    pivot = arr[l]
    while (i < j):
        while arr[i] <= pivot and i <= h:
            i += 1
        while arr[j] > pivot and j >= 0:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    arr[l], arr[j] = arr[j], arr[l]
    return j

def quickSort(arr, l, h):
    if l < h:
        j = partition(arr, l, h)
        quickSort(arr, l, j-1)
        quickSort(arr, j+1, h)
arr = [10, 16, 8, 12, 15, 6, 3, 9, 5]
print(arr)
l = 0
h = len(arr) - 1
quickSort(arr, l, h)
print(arr)
