import heapq
arr = [int(item) for item in input("Enter arr: ").strip().split()]
k = int(input("Enter k: "))
n = len(arr)
maping = {}
for i in range(n):
    if arr[i] not in maping.keys():
        maping[arr[i]] = 1
    else:
        maping[arr[i]] += 1
heap = []
for i in maping.keys():
    heapq.heappush(heap, (maping[i], i))
    if len(heap) > k:
        heapq.heappop(heap)
res = []
while len(heap) > 0:
    res.append(heapq.heappop(heap)[1])
print(res)