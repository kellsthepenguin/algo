def fibo_dp(n):
    cnt = 0
    fibo = [0, 1] + [0] * (n - 1)

    for i in range(2, n + 1):
        fibo[i] = fibo[i - 1] + fibo[i - 2]
        cnt += 1

    return (fibo[n], cnt)

n = int(input())
result, cnt = fibo_dp(n)

print(result, cnt - 1)
