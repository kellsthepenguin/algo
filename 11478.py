import sys

s = sys.stdin.readline().rstrip()
length = 1
strings = set()

while length != len(s):
    for i, letter in enumerate(list(s)):
        strings.add(s[i : i + length])
    length += 1

print(len(strings) + 1)
