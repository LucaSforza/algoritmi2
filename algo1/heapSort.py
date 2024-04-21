import heapq

h = []
heapq.heappush(h,4)
heapq.heappush(h,6)
heapq.heappush(h,8)
print(h)
heapq.heappush(h,4)
heapq.heappush(h,1)


heapq.heappop(h)
print(h)

