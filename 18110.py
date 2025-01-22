import decimal
import sys
from collections import deque


input = sys.stdin.readline

decimal.getcontext().rounding = decimal.ROUND_HALF_UP

n = int(input())
d = []

for _ in range(n):
    d.append(int(input()))

d.sort()
t = int(round(decimal.Decimal(len(d) * 0.15), 0))

deq = deque(d)

for _ in range(t):
    deq.pop()
    deq.popleft()

if len(d) == 0:
    print(0)
    exit()

print(round(decimal.Decimal(sum(deq) / len(deq)), 0))
