class PriorityQueue:
    def __init__(self):
        self.heap = []

    def is_empty(self):
        return len(self.heap) == 0

    def insert(self, item, priority):
        self.heap.append((priority, item))
        self._heapify_up(len(self.heap) - 1)

    def get(self):
        if self.is_empty():
            return None
        item = self.heap[0][1]
        self._swap(0, len(self.heap) - 1)
        self.heap.pop()
        self._heapify_down(0)
        return item

    def _parent(self, child_idx):
        return (child_idx - 1) // 2

    def _children(self, parent_idx):
        left_idx = 2 * parent_idx + 1
        right_idx = left_idx + 1
        return left_idx, right_idx

    def _heapify_up(self, idx):
        parent_idx = self._parent(idx)
        if parent_idx >= 0 and self.heap[parent_idx][0] < self.heap[idx][0]:
            self._swap(parent_idx, idx)
            self._heapify_up(parent_idx)

    def _heapify_down(self, idx):
        max_idx = idx
        left_idx, right_idx = self._children(idx)
        if left_idx < len(self.heap) and self.heap[left_idx][0] > self.heap[max_idx][0]:
            max_idx = left_idx
        if right_idx < len(self.heap) and self.heap[right_idx][0] > self.heap[max_idx][0]:
            max_idx = right_idx
        if max_idx != idx:
            self._swap(max_idx, idx)
            self._heapify_down(max_idx)

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]


# Create an instance of the PriorityQueue class
pq = PriorityQueue()

# Check if the priority queue is empty
print("Is the priority queue empty? " + str(pq.is_empty())) # Outputs: True

# Insert items into the priority queue
pq.insert("eat breakfast", 2)
pq.insert("work", 1)
pq.insert("exercise", 3)
pq.insert("sleep", 0)

# Check if the priority queue is empty
print("Is the priority queue empty? " + str(pq.is_empty())) # Outputs: False



while not pq.is_empty():
# Get items from the priority queue
    print(pq.get())  # Outputs: 'exercise'

# Check if the priority queue is empty
print("Is the priority queue empty? " + str(pq.is_empty())) # Outputs: True
