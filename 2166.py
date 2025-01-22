n = int(input())

x = []
y = []
a = 0

for _ in range(n):
    a, b = map(int, input().split())
    x.append(a)
    y.append(b)

for i in range(1, len(x) + 1):
    a += x[i - 1] * y[i] 

for i in range(1, len(y) + 1):
    a -= x[i] * y[i - 1]

print(abs(a) / 2)
