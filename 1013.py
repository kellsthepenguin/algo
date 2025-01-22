import re
for i in range(int(input())):
    text = input()
    regex = re.compile('(100+1+|01)+')
    if regex.fullmatch(text): print('YES')
    else: print('NO')
