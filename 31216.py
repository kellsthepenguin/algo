def sieve(n):
    arr = [False, False] + [True] * (n - 1)
    primes = []

    for i in range(2, n + 1):
        if arr[i]:
            primes.append(i)
            for j in range(2 * i, n + 1, i):
                arr[j] = False
    
    return primes

t = int(input())
primes = sieve(500000)

for i in range(t):
    n = int(input())

    print(primes[primes[n - 1] - 1])
