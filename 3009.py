x_cnt = {}
y_cnt = {}

for _ in range(3):
    x, y = map(int, input().split())

    if x not in x_cnt.keys():
        x_cnt[x] = 0
    if y not in y_cnt.keys():
        y_cnt[y] = 0
    
    x_cnt[x] += 1
    y_cnt[y] += 1

x_counts = list(x_cnt.values())
y_counts = list(y_cnt.values())


print(list(x_cnt.keys())[x_counts.index(min(x_counts))], list(y_cnt.keys())[y_counts.index(min(y_counts))])
