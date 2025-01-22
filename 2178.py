from collections import deque

n, m = map(int, input().split())
grid = []

for _ in range(n):
    line = list(map(int, list(input())))
    grid.append(line)

visited = set()
to_visit = deque([(0, 0)])

def set_value(arr, x, y, value):
    if x < 0 or y < 0:
        return False
    try:
        if arr[y][x] == 1:
            arr[y][x] = value
        else:
            return False
        return True
    except:
        return False

while to_visit:
    x, y = to_visit.popleft()
    if (x, y) not in visited:
        visited.add((x, y))
        if set_value(grid, x, y + 1, grid[y][x] + 1): #up
            to_visit.append((x, y + 1))
        if set_value(grid, x, y - 1, grid[y][x] + 1): # down
            to_visit.append((x, y - 1))
        if set_value(grid, x - 1, y, grid[y][x] + 1): # left
            to_visit.append((x - 1, y))
        if set_value(grid, x + 1, y, grid[y][x] + 1): # right
            to_visit.append((x + 1, y))

print(grid[n - 1][m - 1])
