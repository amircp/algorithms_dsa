import heapq
new_heap = []


heapq.heappush(new_heap, 2)
heapq.heappush(new_heap, 3)
heapq.heappush(new_heap, 10)
heapq.heappush(new_heap, 7)
heapq.heappush(new_heap, 9)


while new_heap:
    print(heapq.heappop(new_heap))
