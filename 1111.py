import sys

input = sys.stdin.readline
print = sys.stdout.write

n = int(input().rstrip())
nums = list(map(int, input().rstrip().split()))

ok_list = set()

for a in range(-200, 201):
    for b in range(-20000, 20000):
        is_ok = True
        for i in range(n):
            if i + 1 > n - 1: continue
            if (nums[i] * a + b) != nums[i + 1]:
                is_ok = False
                break
        
        if is_ok:
            ok_list.add(nums[-1] * a + b)

length = len(ok_list)

if length > 1:
    print('A')
elif length == 0:
    print('B')
else:
    print(str(ok_list.pop()))
