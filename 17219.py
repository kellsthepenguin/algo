import sys

input = sys.stdin.readline

m, n = map(int, input().rstrip().split())
passwords = {}

for _ in range(m):
    site, pw = input().rstrip().split()
    passwords[site] = pw

for _ in range(n):
    site = input().rstrip()
    print(passwords[site])
