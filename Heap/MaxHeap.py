class maxHeap():
    def __init__(self, length):
        self.maxsize = length
        self.size = 0
        self.FRONT = 0
        self.heap = [0]* (self.maxsize)

    def parent(self, pos):
        return (pos-1) // 2
    def lchild(self, pos):
        return pos*2 + 1
    def rchild(self, pos):
        return pos*2 +2
    def swap(self, a, b):
        self.heap[a], self.heap[b] = self.heap[b], self.heap[a]
    def heapify(self, index):
        lc = self.lchild(index)
        rc = self.rchild(index)
        largest = index
        if self.heap[index] < self.heap[lc] and lc < self.size:
            largest = lc
        if self.heap[largest] < self.heap[rc] and rc < self.size:
            largest = rc
        if largest != index:
            self.swap(largest, index)
            self.heapify(largest)
    def heappush(self, element):
        if self.size >= self.maxsize:
            return
        self.heap[self.size] = element
        curr = self.size
        while curr > 0 and self.heap[self.parent(curr)] < self.heap[curr]:
            self.swap(curr, self.parent(curr))
            curr = self.parent(curr)
        self.size += 1
    def heappop(self):
        if self.size <= 0:
            return
        popped = self.heap[self.FRONT]
        self.heap[self.FRONT] = self.heap[self.size - 1]
        self.size -= 1
        self.heapify(self.FRONT)
        return popped

heap = maxHeap(100)
a = [9,1,2,8,7,3,6,4,5]
for i in a:
    heap.heappush(i)
for i in a:
    print(heap.heappop())
