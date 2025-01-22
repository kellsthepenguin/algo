n, m = map(int, input().split())

balls = []

for l in range(1, n + 1):
    balls.append(l)

for _ in range(m):
    i, j = map(int, input().split())

    balls[i-1:j] = reversed(balls[i-1:j])

print(' '.join(list(map(str, balls))))
