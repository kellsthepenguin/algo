arr = []

for i in range(5):
    arr.append(int(input()))

print(sum(arr) // 5, sorted(arr)[2], sep='\n')
