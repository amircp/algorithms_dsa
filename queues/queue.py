"""
    Practicing Queue

    Most operations in Queues have a O(1) time complexity
"""
class Queue:

    def __init__(self, max_size=3):
        self.queue = []
        self.max_size = max_size

    def insert(self, element):
        if len(self.queue) < self.max_size:
            self.queue.insert(0, element)
        else:
            raise Exception("No space left in queue")

    def remove(self):
        if len(self.queue) < 1:
            raise Exception("No elements left in queue")
        return self.queue.pop(len(self.queue) - 1)


cola = Queue()
cola.insert("1")
cola.insert("2")
cola.insert("3")


stack = []


stack.insert(0, 1)
stack.insert(0, 2)
stack.insert(0, 3)

print(stack.pop())



