n = int(input())

dp = [i for i in range(n+1)]

dp[0] = 0

root_n = int(n**(0.5))

for i in range(n+1):
    for j in range(root_n+1):
        if i+j**2 <= n:
            dp[i+j**2] = min(dp[i]+1, dp[i+j**2])

print(dp)
