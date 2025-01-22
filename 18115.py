from collections import deque

n = int(input())
tasks = list(map(int, input().split()))
first = deque()
tasks.reverse()

for i in range(1, n + 1):
    if tasks[i - 1] == 1:
        first.appendleft(i)
    if tasks[i - 1] == 2:
        first.insert(1, i)
    if tasks[i - 1] == 3:
        first.append(i)

for num in first:
    print(num, end=' ')
