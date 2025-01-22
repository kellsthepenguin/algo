n, m = map(int, input().split())
first = []
second = []
result = []

for i in range(n):
    arr = list(map(int, input().split()))
    first.append(arr)

for i in range(n):
    arr = list(map(int, input().split()))
    second.append(arr)

for i, a in enumerate(first):
    r = []

    for j, b in enumerate(a):
        r.append(b + second[i][j])
    
    result.append(r)

for i in result:
    print(*i)
