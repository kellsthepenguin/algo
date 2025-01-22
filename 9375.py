t = int(input())

for _ in range(t):
    dict = {}
    for __ in range(int(input())):
        name, type = input().split()
        if type not in dict.keys():
            dict[type] = []
        dict[type].append(name)
    cnt = 1
    for wear in dict:
        cnt *= (len(dict[wear]) + 1)
    
    print(cnt - 1)
