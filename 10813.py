from copy import copy

n, m = map(int, input().split())

balls = []

for l in range(1, n + 1):
    balls.append(l)

for _ in range(m):
    i, j = map(int, input().split())

    iValue = int(balls[i - 1])
    jValue = int(balls[j - 1])

    balls[i - 1] = jValue
    balls[j - 1] = iValue

print(' '.join(list(map(str, balls))))
