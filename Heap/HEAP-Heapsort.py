import sys
class MaxHeap:
    def __init__(self, maxzize):
        self.maxsize = maxzize
        self.size = 0
        self.heap = [0] * (self.maxsize)
        self.FRONT = 0

    def parent(self, pos):
        return (pos-1)//2

    def leftChild(self, pos):
        return (2*pos) + 1

    def rightChild(self, pos):
        return (2*pos) + 2

    def isLeaf(self, pos):
        return True if pos >= self.size//2 and pos <= self.size else False

    def swap(self, a, b):
        self.heap[a], self.heap[b] = (self.heap[b], self.heap[a])

    def maxHeapify(self, pos):
        l = self.leftChild(pos)
        r = self.rightChild(pos)
        largest = pos
        if (self.heap[pos] < self.heap[l] and l < self.size):
            largest = l
        if (self.heap[largest] < self.heap[r] and r < self.size):
            largest = r
        if largest != pos:  
            self.swap(pos, largest)
            self.maxHeapify(pos)

    def heap_push(self, element):
        if self.size >= self.maxsize:
            return
        self.heap[self.size] = element
        curr = self.size
        self.size += 1
        while (self.heap[curr] > self.heap[self.parent(curr)] and curr > 0):
            self.swap(curr, self.parent(curr))
            curr = self.parent(curr)

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

    def heapSort(self):
        for i in range(self.size // 2 - 1, -1, -1):
            self.maxHeapify(i)
        for i in range(self.size-1, 0, -1):
            self.swap(0, i)
            self.size -= 1
            self.maxHeapify(0)


if __name__ == "__main__":
    print('The maxHeap is ')

    maxHeap = MaxHeap(15)
    maxHeap.heap_push(5)
    maxHeap.heap_push(3)
    maxHeap.heap_push(17)
    maxHeap.heap_push(10)
    maxHeap.heap_push(84)
    maxHeap.heap_push(19)
    maxHeap.heap_push(6)
    maxHeap.heap_push(22)
    maxHeap.heap_push(9)
    maxHeap.Print()
    maxHeap.heapSort()
    maxHeap.Print()