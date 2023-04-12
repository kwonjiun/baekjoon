n = int(input())

dp = [i for i in range(n+1)]

dp[0] = 0

for i in range(2,n+1):
    if i**(0.5)%1 == 0:
        dp[i] = 1
        continue
    for j in range(1,int(i**(0.5))+1):
        dp[i] = min(dp[i],dp[i-j**2] + 1)

print(dp[-1])