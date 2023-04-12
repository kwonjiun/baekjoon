import sys

input = sys.stdin.readline

n = int(input())

cost = [list(map(int,input().split())) for _ in range(n)]

dp = [[0,0,0] for _ in range(n)]

dp[0] = cost[0].copy()
for i in range(1,n):
    for j in range(3):
        if j == 0:
            dp[i][j] = min(dp[i-1][1],dp[i-1][2]) + cost[i][j]
        elif j == 1:
            dp[i][j] = min(dp[i-1][0],dp[i-1][2]) + cost[i][j]
        elif j == 2:
            dp[i][j] = min(dp[i-1][0],dp[i-1][1]) + cost[i][j]

print(min(dp[-1]))