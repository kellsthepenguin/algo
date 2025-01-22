from collections import deque

c = int(input())
edges = int(input())
graph = {}

for _ in range(edges):
    v1, v2 = map(int, input().split())
    if v1 not in graph.keys():
        graph[v1] = []
    if v2 not in graph.keys():
        graph[v2] = []
    
    graph[v1].append(v2)
    graph[v2].append(v1)

def bfs(graph, start):
    visited = []
    to_visit = deque([start])

    while to_visit:
        node = to_visit.popleft()
        if node not in visited:
            visited.append(node)
            to_visit.extend(sorted(graph[node]))

    return visited

if 1 not in graph.keys():
    print(0)
    exit()

print(len(bfs(graph, 1)) - 1)
