import sys
import heapq

input = sys.stdin.readline
heap = []

n = int(input().rstrip())

for i in range(n):
    command = int(input().rstrip())

    if command == 0:
        if len(heap) == 0:
            print(0)
            continue
        print(abs(heapq.heappop(heap)))
    else:
        heapq.heappush(heap, -command)
