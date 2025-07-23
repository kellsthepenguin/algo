n, k = map(int, input().split())
x = list(map(int, input().split()))

print(list(reversed(sorted(x)))[k - 1])
