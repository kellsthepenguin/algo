from collections import deque

m, n, h = map(int, input().split())

visited = set()
to_visit = deque()
dimension = []

def set_value(arr, x, y, z, value):
    if x < 0 or y < 0:
        return False
    try:
        if arr[z][y][x] == 0:
            arr[z][y][x] = value
        else:
            return False
        return True
    except:
        return False

for i in range(n):
    line = list(map(int, input().split()))
    dimension.append(line)
    dimension = dimension * h

for z, grid in enumerate(dimension):
    for y, line in enumerate(grid):
        for x, tomato in enumerate(line):
            if tomato == 1:
                to_visit.append((x, y, z))

while to_visit:
    x, y, z = to_visit.popleft()
    if (x, y, z) not in visited:
        visited.add((x, y, z))
        if set_value(dimension, x, y + 1, z, dimension[y][x] + 1): # front
            to_visit.append((x, y + 1))
        if set_value(dimension, x, y - 1, z, dimension[y][x] + 1): # down
            to_visit.append((x, y - 1))
        if set_value(dimension, x - 1, y, z, dimension[y][x] + 1): # left
            to_visit.append((x - 1, y))
        if set_value(dimension, x + 1, y, z, dimension[y][x] + 1): # right
            to_visit.append((x + 1, y))

days = 0
for grid in dimension:
    for line in grid:
        for tomato in line:
            if tomato == 0:
                print(-1)
                exit()
            days = max(days, max(line))

print(days - 1)