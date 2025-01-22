from collections import deque

m, n = map(int, input().split())

visited = set()
to_visit = deque()
grid = []

def set_value(arr, x, y, value):
    if x < 0 or y < 0:
        return False
    try:
        if arr[y][x] == 0:
            arr[y][x] = value
        else:
            return False
        return True
    except:
        return False

for i in range(n):
    line = list(map(int, input().split()))
    grid.append(line)

for y, line in enumerate(grid):
    for x, tomato in enumerate(line):
        if tomato == 1:
            to_visit.append((x, y))

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

days = 0
for line in grid:
    for tomato in line:
        if tomato == 0:
            print(-1)
            exit()
    days = max(days, max(line))

print(days - 1)
