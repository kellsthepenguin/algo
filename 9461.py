dp = [1, 1, 1] + [0] * 100

for i in range(3, 101):
    dp[i] = dp[i - 2] + dp[i - 3]

t = int(input())

for _ in range(t):
    print(dp[int(input()) - 1])
