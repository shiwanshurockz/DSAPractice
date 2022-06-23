class MaxHeap:
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.size = 0
        self.heap = [0] * self.maxsize
        self.FRONT = 0

    def parent(self, pos):
        return (pos-1) // 2
    def leftChild(self, pos):
        return (pos * 2) + 1
    def rightChild(self, pos):
        return (pos * 2) + 2
    def swap(self, a, b):
        self.heap[a], self.heap[b] = (self.heap[b], self.heap[a])
    def maxHeapify(self, pos):
        l = (2*pos) + 1
        r = (2*pos) + 2
        largest = pos
        if self.heap[pos] < self.heap[l] and l < self.size:
            largest = l
        if self.heap[largest] < self.heap[r] and r < self.size:
            largest = r
        if largest != pos:
            self.swap(pos, largest)
            self.maxHeapify(largest)
    def heap_push(self, element):
        if self.size >= self.maxsize:
            return
        self.heap[self.size] = element
        curr = self.size
        while (curr > 0 and self.heap[curr] > self.heap[self.parent(curr)]):
            self.swap(curr, self.parent(curr))
            curr = self.parent(curr)
        self.size += 1
    def heap_pop(self):
        popped = self.heap[self.FRONT]
        self.heap[self.FRONT] = self.heap[self.size-1]
        self.size -= 1
        self.maxHeapify(self.FRONT)
        return popped
    def Print(self):
        for i in range((self.size//2)+1):
            print("Parent :"+str(self.heap[i])
                  + "Left Child :"+str(self.heap[self.leftChild(i)])
                  + "Right child: "+str(self.heap[self.rightChild(i)]) )


arr1 = [int(item) for item in input().strip().split()]
k = int(input())
maxHeap = MaxHeap(15)
for i in range(len(arr1)):
    maxHeap.heap_push(arr1[i])
kthelement = 0
for j in range(len(arr1) - k + 1):
    kthelement = maxHeap.heap_pop()
print(kthelement)