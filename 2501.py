n, k = map(int, input().split())
divisors = []

for i in range(1, n + 1):
    if n % i == 0:
        divisors.append(i)

try:
    print(divisors[k - 1])
except:
    print(0)
