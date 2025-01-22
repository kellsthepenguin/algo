import sys

input = sys.stdin.readline

n, m = map(int, input().split())

dict = {}

for i in range(1, n + 1):
    name = input().rstrip()

    dict[name] = i

keys = list(dict.keys())

for _ in range(m):
    ipt = input().rstrip()

    if ipt.isdigit():
        print(keys[int(ipt) - 1])
    else:
        print(dict[ipt])
