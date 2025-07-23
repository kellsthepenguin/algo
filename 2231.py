n = int(input())

for i in range(n):
    if i + sum(map(int, list(str(i)))) == n:
        print(i)
        exit()

print(0)
