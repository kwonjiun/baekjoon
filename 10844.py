import sys

input = sys.stdin.readline

n = int(input())

dp = [[0 for i in range(10)] for i in range(100+1)]

dp[1] = [0,1,1,1,1,1,1,1,1,1]
mod = 1_000_000_000
for i in range(2,101):
    dp[i][0] = dp[i-1][1] %mod
    dp[i][1] = (dp[i-1][0]+dp[i-1][2]) %mod
    dp[i][2] = (dp[i-1][1]+dp[i-1][3]) %mod
    dp[i][3] = (dp[i-1][2]+dp[i-1][4]) %mod
    dp[i][4] = (dp[i-1][3]+dp[i-1][5]) %mod
    dp[i][5] = (dp[i-1][4]+dp[i-1][6]) %mod
    dp[i][6] = (dp[i-1][5]+dp[i-1][7]) %mod
    dp[i][7] = (dp[i-1][6]+dp[i-1][8]) %mod
    dp[i][8] = (dp[i-1][7]+dp[i-1][9]) %mod
    dp[i][9] = (dp[i-1][8])%mod

print(sum(dp[n])%mod)