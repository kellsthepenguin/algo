import itertools
w = 0
b = 0

def dnc(s):
    global w, b
    l = len(s)
    if l == 1: return
    h1 = s[0:(l // 2)]
    h2 = s[(l // 2):l]
    ss = [[], [], [], []]

    for l1 in h1:
        ss[0].append(l1[0:(l // 2)])
        ss[1].append(l1[(l // 2):l])
    
    for l2 in h2:
        ss[2].append(l2[0:(l // 2)])
        ss[3].append(l2[(l // 2):l])

    for i, sq in enumerate(ss):
        chained = list(itertools.chain.from_iterable(sq))

        if chained.count(0) == len(chained):
            w += 1
            ss[i] = [[5] * (l // 2)] * (l // 2)
        elif chained.count(1) == len(chained):
            b += 1
            ss[i] = [[5] * (l // 2)] * (l // 2)

        dnc(ss[i])


n = int(input())
square = []

for _ in range(n):
    square.append(list(map(int, input().split())))

flatten = sum(square, [])

if flatten.count(0) == len(flatten):
    print(1)
    print(0)
    exit()
elif flatten.count(1) == len(flatten):
    print(0)
    print(1)
    exit()

dnc(square)

print(w)
print(b)
