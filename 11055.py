import sys

input = sys.stdin.readline

n = int(input())

numbers = list(map(int,input().split()))
dp = [0]*1000

dp[0] = numbers[0]
for i in range(1,n):
    for j in range(i):
        if numbers[i] > numbers[j]:
            dp[i] = max(dp[j] + numbers[i],dp[i])
print(dp)
            