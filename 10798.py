arr = []
for _ in range(5):
    arr.append(list(input()))

for i in range(15):
    for j in range(5):
        if i < len(arr[j]):
            print(arr[j][i], end='')
