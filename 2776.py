from bisect import bisect_left

t = int(input())

for _ in range(t):
    n = int(input())
    diary1 = list(map(int, input().split()))
    m = int(input())
    diary2 = list(map(int, input().split()))

    sortedDiary1 = sorted(diary1)

    for num in diary2:
        index = bisect_left(sortedDiary1, num)

        if index == len(sortedDiary1) or sortedDiary1[index] != num:
            print(0)
        else:
            print(1)
