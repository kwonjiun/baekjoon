import sys

input = sys.stdin.readline

n = int(input())

cost = []
for i in range(n):
    cost.append(int(input()))

dp = [0]*n
dp[0] = cost[0]
if n>=2:
    dp[1] = cost[0] + cost[1]
if n >= 3:
    dp[2] = max(cost[0]+cost[2] , cost[1]+cost[2],cost[0]+cost[1])
if n>=4:
    for i in range(3,n):
        dp[i] = max(dp[i-1], cost[i]+dp[i-2], cost[i]+cost[i-1]+dp[i-3])

print(dp[-1])
