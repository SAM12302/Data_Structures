class MaxHeap:
    def __init__(self, array=None):
        if array is None:
            self.heap = []
        else:
            self.heap = array
            self.build_heap()

    def build_heap(self):
        n = len(self.heap)
        # start from last parent and sift down
        for i in range((n // 2) - 1, -1, -1):
            self.sift_down(i)

    def sift_down(self, i):
        size = len(self.heap)
        max_index = i

        left = 2 * i + 1
        right = 2 * i + 2

        if left < size and self.heap[left] > self.heap[max_index]:
            max_index = left
        if right < size and self.heap[right] > self.heap[max_index]:
            max_index = right

        if i != max_index:
            self.heap[i], self.heap[max_index] = self.heap[max_index], self.heap[i]
            self.sift_down(max_index)

    def sift_up(self, i):
        while i > 0:
            parent = (i - 1) // 2
            if self.heap[i] > self.heap[parent]:
                self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
                i = parent
            else:
                break

    def insert(self, value):
        self.heap.append(value)
        self.sift_up(len(self.heap) - 1)

    def extract_max(self):
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.sift_down(0)
        return root

    def change_priority(self, index, new_value):
        old_value = self.heap[index]
        self.heap[index] = new_value
        if new_value > old_value:
            self.sift_up(index)
        else:
            self.sift_down(index)

    def remove(self, index):
        self.change_priority(index, float("inf"))
        self.sift_up(index)
        self.extract_max()

    def __str__(self):
        return str(self.heap)


# Example usage
if __name__ == "__main__":
    heap = MaxHeap([5, 3, 8, 4, 1])
    print("Initial heap:", heap)

    heap.insert(0)
    print("After insert 0:", heap)

    print("Extract max:", heap.extract_max())
    print("Heap after extract:", heap)

    heap.change_priority(2, 10)
    print("After change priority index 2 → 10:", heap)

    heap.remove(1)
    print("After remove index 1:", heap)
