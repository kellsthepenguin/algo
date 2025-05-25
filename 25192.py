n = int(input())

g = {}
go = 0

for i in range(n):
    name = input()
    if name == 'ENTER':
        g = {}
        continue
    try:
        g[name]
    except:
        g[name] = 'o'
        go += 1

print(go)
