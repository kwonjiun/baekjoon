import sys

input = sys.stdin.readline

n = int(input())

cost = [list(map(int,input().split())) for _ in range(n)]

dp = [[0,0,0] for _ in range(n)]

answer = 1000 * 1000

for i in range(3):
    dp[0] = [1000,1000,1000]
    dp[0][i] = cost[0][i]
    for j in range(1,n):
        dp[j][0] = min(dp[j-1][1], dp[j-1][2]) + cost[j][0]  
        dp[j][1] = min(dp[j-1][2], dp[j-1][0]) + cost[j][1]
        dp[j][2] = min(dp[j-1][1], dp[j-1][0]) + cost[j][2]
    for k in range(3):
        if i != k:
            answer = min(answer,dp[-1][k])
print(answer)
