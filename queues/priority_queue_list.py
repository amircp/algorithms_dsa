"""
    Practicing priority queue using lists

    Using this implementation we have a time complexity of O(n Log n)
"""

queue = list()

queue.append((1, "Amir"))
queue.append((4, "Walter"))
queue.append((10, "Rafa"))
queue.append((6, "Moises"))

# max-heap
queue.sort(reverse=True)
queue.sort()

while queue:
    print(f"Priority Queue = {queue.pop()}")