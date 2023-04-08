import sys

input = sys.stdin.readline

n = int(input())

cost = [0] + list(map(int,input().split()))

dp = cost.copy()

for i in range(1,n+1):
    for j in range(i+1):
        dp[i] = min(dp[i-j] + dp[j], dp[i])

print(dp[-1])
