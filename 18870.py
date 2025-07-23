input()
x = list(map(int, input().split()))
sx = sorted(list(set(x)))
dict = {}

for i, n in enumerate(sx):
    dict[n] = i

for num in x:
    print(dict[num], end=' ')
