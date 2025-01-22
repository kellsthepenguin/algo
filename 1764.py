import sys

input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
d = set()
b = set()

for i in range(n):
    d.add(input().rstrip())

for i in range(m):
    b.add(input().rstrip())

db = []

for d_name in d:
    if d_name in b:
        db.append(d_name)

print(len(db))

db.sort()

for db_name in db:
    print(db_name)
