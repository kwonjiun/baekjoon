import sys

input = sys.stdin.readline

n = int(input())

numbers = list(map(int,input().split()))

dp = [1 for _ in range(n)]

for i in range(n):
    for j in range(i):
        if numbers[i] > numbers[j] and dp[i] <dp[j]+1:
            dp[i] = dp[j]+1

print(max(dp))
