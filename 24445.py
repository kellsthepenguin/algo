import sys
from collections import deque

input = sys.stdin.readline

n, m, r = map(int, input().split())
graph = [[] for _ in range(n + 1)]

def bfs(graph, start):
    visited = set()
    to_visit = deque([start])
    order = {}
    curr = 0

    while to_visit:
        node = to_visit.popleft()
        if node not in visited:
            visited.add(node)
            curr += 1
            order[node] = curr
            to_visit.extend(graph[node])

    return order


for _ in range(m):
    v1, v2 = map(int, input().split())
    
    graph[v1].append(v2)
    graph[v2].append(v1)

for i in range(len(graph)):
    graph[i].sort()
    graph[i].reverse()

bfs_result = bfs(graph, r)

for i in range(1, n + 1):
    print(bfs_result.get(i, 0))
