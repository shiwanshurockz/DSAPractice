import heapq

def negate(n):
    return -1 * n

arr1 = [int(item) for item in input().strip().split()]
arr1 = list(map(negate, arr1))
heapq.heapify(arr1)
n = len(arr1)
while (n > 1):
    first = heapq.heappop(arr1)
    second = heapq.heappop(arr1)
    remaining = abs(first - second)
    if remaining == 0:
        n -= 2
    else:
        heapq.heappush(arr1, -1 * remaining)
        n -= 1
if not arr1:
    print(0)
else:
    print(-1 * arr1[0])
