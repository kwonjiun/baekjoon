import sys

input = sys.stdin.readline

n = int(input())

numbers = list(map(int,input().split()))
dp = numbers.copy()
for i in range(1,n):
    for j in range(i):
        if numbers[i] > numbers[j]:
            dp[i] = max(dp[j] + numbers[i],dp[i])
print(max(dp))
            