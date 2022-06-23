arr = [int(item) for item in input("ENter elements :").split()]
N = len(arr)
K = int(input('Element to be searched for :'))

def terbarySearch(arr, N, K):
    return search(arr, 0, N, K)


def search(arr, l, r, k):
    if r >= l:
        mid1 = l + (r-l)//3
        mid2 = r - (r-l)//3
        if k == arr[mid1]:
            return 1
        if k == arr[mid2]:
            return 1
        if k < arr[mid1]:
            return search(arr, 0, mid1-1, k)
        if k > arr[mid2]:
            return search(arr, mid2+1, r, k)
        else:
            return search(arr, mid1+1, mid2-1, k)
    return -1

print(terbarySearch(arr, N, K))
