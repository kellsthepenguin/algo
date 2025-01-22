def f(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    bridges = f(m) // (f(n) * f(m - n))
    print(bridges)
