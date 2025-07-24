from collections import deque

k = int(input())
a = deque()

for i in range(k):
    c = int(input())

    if c == 0:
        a.pop()
    else:
        a.append(c)

print(sum(a))
