from math import sqrt

t = int(input())

for i in range(t):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    d = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

    if abs(r2 - r1) < d < (r2 + r1):
        print(2)
    elif x1 == x2 and y1 == y2 and r1 == r2:
        print(-1)
    elif r1 + r2 == d or abs(r2 - r1) == d:
        print(1)
    elif r1 + r2 < d or d < abs(r2 - r1) or d == 0:
        print(0)
