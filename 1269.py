input()
a = set(list(map(int, input().split())))
b = set(list(map(int, input().split())))

print(len(a.symmetric_difference(b)))
