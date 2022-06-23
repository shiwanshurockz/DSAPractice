class MaxHeap:
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.heap = [0] * self.maxsize
        self.size = 0
        self.FRONT = 0
    def parent(self, pos):
        return (pos-1)//2

    def leftchild(self, pos):
        return (pos * 2)+1

    def rightchild(self, pos):
        return (pos * 2) +2

    def swap(self,a,b):
        self.heap[a], self.heap[b] = self.heap[b], self.heap[a]

    def maxHeapify(self, pos):
        l = self.leftchild(pos)
        r = self.rightchild(pos)
        largest = pos
        if self.heap[pos] < self.heap[l] and l < self.size:
            largest = l
        if self.heap[largest] < self.heap[r] and r < self.size:
            largest = r
        if largest != pos:
            self.swap(pos, largest)
            self.maxHeapify(largest)

    def push(self, element):
        if self.size >= self.maxsize:
            return
        self.heap[self.size] = element
        curr = self.size
        while (curr > 0 and self.heap[curr] > self.heap[self.parent(curr)]):
            self.swap(curr, self.parent(curr))
            curr = self.parent(curr)
        self.size += 1
    def pop(self):
        popped = self.heap[self.FRONT]
        self.heap[self.FRONT] = self.heap[ self.size-1]
        self.size -= 1
        self.maxHeapify(self.FRONT)

        return popped


T = int(input())
res = []
for i in range(T):
    N, K = (int(item) for item in input().split())
    arr = [int(item) for item in input().split()]
    result = ""
    maxHeap = MaxHeap(100)
    for i in range(N):
        maxHeap.push(-1 * arr[i])
        if maxHeap.size > K:
            var = -1 * maxHeap.pop()
            result += str(var) + " "
    for j in range(maxHeap.size):
        var = -1 * maxHeap.pop()
        result += str(var) + " "
    res.append(var)
for i in res:
    print(i)
