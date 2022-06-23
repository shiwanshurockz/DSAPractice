class MaxHeap:
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.size = 0
        self.FRONT = 0
        self.Heap = [(0, 0)] * self.maxsize
    def parent(self, pos):
        return (pos-1)//2
    def lc(self, pos):
        return (pos*2)+1
    def rc(self, pos):
        return (pos*2)+2
    def swap(self, a, b):
        self.Heap[a], self.Heap[b] = self.Heap[b],self.Heap[a]
    def MaxHeapify(self, pos):
        l = self.lc(pos)
        r = self.rc(pos)
        largest = pos
        if self.Heap[pos][0] < self.Heap[l][0] and l < self.size:
            largest = l
        if self.Heap[largest][0] < self.Heap[r][0] and r < self.size:
            largest = r
        if largest != pos:
            self.swap(pos,largest)
            self.MaxHeapify(largest)
    def heap_push(self, element):
        if self.size >= self.maxsize:
            return
        self.Heap[self.size] = element
        currr = self.size
        self.size += 1
        while (currr > 0 and self.Heap[currr][0] > self.Heap[self.parent(currr)][0]):
            self.swap(currr, self.parent(currr))
            currr = self.parent(currr)
    def heap_pop(self):
        popped = self.Heap[self.FRONT]
        self.Heap[self.FRONT] = self.Heap[self.size-1]
        self.size -= 1
        self.MaxHeapify(self.FRONT)
        return popped
arr = [int(item) for item in input().strip().split()]
maxhp = MaxHeap(100)
n = len(arr)
x = int(input("Enter x:"))
k = int(input("Enter k: "))
for i in range(n):
    if arr[i] != x:
        maxhp.heap_push((abs(arr[i] - x), arr[i]))
        if maxhp.size > k:
            maxhp.heap_pop()
res = []
while(maxhp.size > 0):
    popped = maxhp.heap_pop()
    res.append(popped[1])
print(res)