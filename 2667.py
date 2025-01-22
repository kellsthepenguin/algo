from collections import deque

n = int(input())
grid = [list(map(int, list(input().strip()))) for _ in range(n)]

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def bfs(x, y, cnt):
    queue = deque([(x, y)])
    grid[y][x] = cnt
    size = 1

    while queue:
        cx, cy = queue.popleft()
        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < n and 0 <= ny < n and grid[ny][nx] == 1:
                grid[ny][nx] = cnt
                queue.append((nx, ny))
                size += 1

    return size

cnt = 2
sizes = []

for y in range(n):
    for x in range(n):
        if grid[y][x] == 1:
            sizes.append(bfs(x, y, cnt))
            cnt += 1

sizes.sort()
print(len(sizes))
for size in sizes:
    print(size)
