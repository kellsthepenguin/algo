import statistics

n = int(input())
nums = []

for i in range(n):
    nums.append(int(input()))

print(round(statistics.mean(nums)))
print(statistics.median(nums))

modes = statistics.multimode(nums)

if len(modes) >= 2:
    print(sorted(modes)[1])
else:
    print(modes[0])

print(abs(max(nums) - min(nums)))
