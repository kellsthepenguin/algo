arr = []

for _ in range(9):
    arr.append(list(map(int, input().split())))

max_values = list(map(max, arr))
max_value = max(max_values)

row = max_values.index(max_value)
column = arr[row].index(max_value)

print(max_value)
print(row+1, column+1)
