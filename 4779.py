def c(n):
    if n == 1: return '-'

    l = c(n // 3)
    ct = ' ' * (n // 3)

    return l + ct + l

while True:
    try:
        print(c(3 ** int(input())))
    except:
        break
