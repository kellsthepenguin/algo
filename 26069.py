n = int(input())

dancers = set(['ChongChong'])

for i in range(n):
    names = input().split()

    for name in names:
        if name in dancers:
            for n in names:
                dancers.add(n)

print(len(dancers))
