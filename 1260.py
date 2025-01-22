from collections import deque

def dfs(graph, start):
    visited = []
    to_visit = deque([start])

    while to_visit:
        node = to_visit.pop()
        if node not in visited:
            visited.append(node)
            to_visit.extend(sorted(graph[node]).__reversed__())

    return visited

def bfs(graph, start):
    visited = []
    to_visit = deque([start])

    while to_visit:
        node = to_visit.popleft()
        if node not in visited:
            visited.append(node)
            to_visit.extend(sorted(graph[node]))

    return visited

n, m, v = map(int, input().split())
graph = {}

for i in range(m):
    v1, v2 = map(int, input().split())
    if v1 not in graph.keys():
        graph[v1] = []
    if v2 not in graph.keys():
        graph[v2] = []
    
    graph[v1].append(v2)
    graph[v2].append(v1)

if v not in graph.keys():
    print(v)
    print(v)
    exit()

print(' '.join(str(s) for s in dfs(graph, v)))
print(' '.join(str(s) for s in bfs(graph, v)))
