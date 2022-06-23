arr = [int(item) for item in input("Enter arr1: ").strip().split()]
n = len(arr)
def LDS(arr):
    n = len(arr)
    LIS = [1 for i in range(n)]
    for i in range(n-1, -1, -1):
        for j in range(i+1, n):
            if arr[i] > arr[j]:
                LIS[i] = max(LIS[i], 1+LIS[j])
    return LIS

def LIS(arr):
    n = len(arr)
    LIS = [1 for i in range(n)]
    for i in range(n):
        for j in range(0, i):
            if arr[i] > arr[j]:
                LIS[i] = max(LIS[i], 1+LIS[j])
    return LIS

lis, lds = (LIS(arr), LDS(arr))
res = []
for i in range(n):
    res.append(lis[i] + lds[i] - 1)
print(max(res))