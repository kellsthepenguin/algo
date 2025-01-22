a, b, c, d, e, f = map(int, input().split())

x = 0
y = 0

if a == 0:
    y = c / b
    x = (f - e * y) / d
else:
    y = (a * f - d * c) / (a * e - b * d)
    x = c / a - (b * y / a)

print(int(x), int(y))
