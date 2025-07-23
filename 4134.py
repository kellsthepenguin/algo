def f(x):
    nums = []
    for i in range(1, int(x**0.5) + 1):
        if x % i == 0:
            nums.append(i)
    
    for k in nums.copy():
        nums.append(x // k)

    return len(set(nums))

t = int(input())

for i in range(t):
    n = int(input())

    while True:
        if f(n) == 2:
            print(n)
            break
        
        n += 1
