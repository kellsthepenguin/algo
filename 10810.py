n, m = map(int, input().split())
balls = [0] * n

for _ in range(m):
    i, j, k = map(int, input().split())

    balls[i-1:j] = [k] * ((j - i) + 1)

print(' '.join(list(map(str, balls))))
