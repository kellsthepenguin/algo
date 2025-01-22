t = int(input())

yonsei = 0
korea = 0

for i in range(t):
    yonsei = 0
    korea = 0

    for j in range(9):
        y, k = map(int, input().split())

        yonsei += y
        korea += k

    if yonsei == korea:
        print('Draw')
    elif yonsei > korea:
        print('Yonsei')
    elif korea > yonsei:
        print('Korea')
