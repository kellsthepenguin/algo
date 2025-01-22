t = int(input())

for i in range(t):
    n = int(input())
    cnts = {
        0: (1, 0),
        1: (0, 1)
    }

    for i in range(2, n + 1):
        cnts[i] = (cnts[i - 1][0] + cnts[i - 2][0], cnts[i - 1][1] + cnts[i - 2][1])

    print(str(cnts[n]).removeprefix('(').removesuffix(')').replace(',', ''))
