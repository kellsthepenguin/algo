import sys

t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    p = sys.stdin.readline().rstrip()
    n = int(sys.stdin.readline().rstrip())
    strArr = sys.stdin.readline().rstrip()
    arr = []

    if strArr == '[]':
        arr = []
    else:
        arr = list(map(int, strArr[1:-1].split(',')))

    isReversed = False
    result = ''

    for c in list(p):
        if result == 'error': continue
        if c == 'R': isReversed = not isReversed
        if c == 'D':
            if len(arr) == 0:
                result = 'error'
                continue
            if isReversed: arr = arr[0:-1]
            else: arr = arr[1:]
    
    if isReversed: arr.reverse()
    if result == '': result = str(arr).replace(' ', '')

    print(result)
