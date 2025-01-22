from itertools import chain

n = int(input())
k = int(input())

A = [[0] * n] * n

for i, a in enumerate(A):
    for j, b in enumerate(a):
        A[i][j] = (i + 1) * (j + 1)

arr = list(chain.from_iterable(A))

print(A)

print(sorted(arr)[k-1])
