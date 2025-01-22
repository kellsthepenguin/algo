from math import sqrt

t = int(input())

for _ in range(t):
    x, y = map(int, input().split())
    distance = y - x
    d = 3
    next = 3

    n = int(sqrt(distance))
    if distance == n ** 2:
        print(2 * n - 1)
    elif distance <= n ** 2 + n:
        print(2 * n)
    else:
        print(2 * n + 1)
