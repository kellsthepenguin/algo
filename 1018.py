n, m = map(int, input().split())
c = []
fw = [['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']]
fb = [['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B']]

for _ in range(n):
    c.append(list(input()))

s = []

for y in range(0, n):
    for x in range(0, m):
        try:
            c[y + 7][x + 7]
            s.append((y, x))
        except:
            pass

mini = 64

for y, x in s:
    c_fw = 0
    c_fb = 0

    for i in range(0, 8):
        for j in range(0, 8):
            if c[y + i][x + j] != fw[i][j]:
                c_fw += 1
            if c[y + i][x + j] != fb[i][j]:
                c_fb += 1

    if c_fw < mini:
        mini = c_fw
    if c_fb < mini:
        mini = c_fb

print(mini)
