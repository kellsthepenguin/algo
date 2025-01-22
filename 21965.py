_ = input()
seq = list(map(int, input().split()))
maxValue = max(seq)
maxIndex = seq.index(maxValue)

if seq.count(maxValue) > 1:
    print('NO')
    exit()


def is_increasing(arr):
    return all(arr[i] < arr[i + 1] for i in range(len(arr) - 1))


def is_decreasing(arr):
    return all(arr[i] > arr[i + 1] for i in range(len(arr) - 1))

smaller_values_than_max = seq[0:maxIndex]

if not is_increasing(smaller_values_than_max):
    print('NO')
    exit()

bigger_values_than_max = seq[maxIndex + 1:]

if not is_decreasing(bigger_values_than_max):
    print('NO')
    exit()

print('YES')
