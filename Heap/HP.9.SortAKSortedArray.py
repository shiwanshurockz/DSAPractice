"""
Heaps And Maps
Merge K Sorted Arrays!
"""

A = [[1, 2, 3], [4, 5, 6], [7, 8, 9] ]

import heapq
def solve(A):
    res = []
    n = len(A)
    m = len(A[0])
    heap = []
    for i in range(n):
        heapq.heappush(heap, A[i])
    while (len(heap) > 0):
        popped = heapq.heappop(heap)
        if len(popped) > 1:
            elem = popped.pop(0)
            heapq.heappush(heap, popped)
            res.append(elem)
        else:
            elem = popped.pop(0)
            res.append(elem)
    return res
print(solve(A))