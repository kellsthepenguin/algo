t = int(input())

for _ in range(t):
    h, w, n = map(int, input().split())
    
    x = n % h
    y = n / h + 1

    if x == 0:
        x = h
        y -= 1
    
    print("%d%02d" % (x, y))
