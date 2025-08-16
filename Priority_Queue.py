class PriorityQueue:
    def __init__(self):
        self.heap = []

    def parent(self, i):
        return (i - 1) // 2

    def left(self, i):
        return 2 * i + 1

    def right(self, i):
        return 2 * i + 2

    def push(self, value):
        self.heap.append(value)
        i = len(self.heap) - 1
        while i > 0 and self.heap[self.parent(i)] > self.heap[i]:
            self.heap[self.parent(i)], self.heap[i] = self.heap[i], self.heap[self.parent(i)]
            i = self.parent(i)

    def heapify(self, i):
        smallest = i
        l = self.left(i)
        r = self.right(i)

        if l < len(self.heap) and self.heap[l] < self.heap[smallest]:
            smallest = l
        if r < len(self.heap) and self.heap[r] < self.heap[smallest]:
            smallest = r

        if smallest != i:
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            self.heapify(smallest)

    def pop(self):
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.heapify(0)
        return root

    def peek(self):
        return None if not self.heap else self.heap[0]

    def is_empty(self):
        return len(self.heap) == 0

    def __str__(self):
        return str(self.heap)

pq = PriorityQueue()
pq.push(19)
pq.push(14)
pq.push(28)
pq.push(15)
pq.push(16)
pq.push(7)

print("Heap:", pq)         # Internal heap
print("Peek:", pq.peek())  # Smallest element
print("Pop:", pq.pop())    # Remove smallest
print("Heap after pop:", pq)
