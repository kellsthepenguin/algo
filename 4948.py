def sieves(m, n):
    arr = [False, False] + [True] * (n - 1)
    primes = []

    for i in range(2, n + 1):
        if arr[i]:
            for j in range(2 * i, n + 1, i):
                arr[j] = False

    for i, is_prime in enumerate(arr):
        if is_prime and i >= m:
            primes.append(i)

    return primes

while True:
    n = int(input())
    if n == 0: exit()
    primes = sieves(n, 2 * n)

    if n in primes:
        print(len(primes) - 1)
    else:
        print(len(primes))
