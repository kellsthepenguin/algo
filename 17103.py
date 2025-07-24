def sieves(n):
    arr = [False, False] + [True] * (n - 1)
    primes = set()

    for i in range(2, n + 1):
        if arr[i]:
            for j in range(2 * i, n + 1, i):
                arr[j] = False

    for i, is_prime in enumerate(arr):
        if is_prime:
            primes.add(i)

    return primes

t = int(input())

for i in range(t):
    n = int(input())
    parts = set()
    primes = sieves(n)

    for prime in primes:
        if n - prime in primes:
            parts.add(tuple(sorted((prime, n - prime))))

    print(len(parts))
