import sys

input = sys.stdin.readline

n = int(input())

numbers= []
for i in range(n):
    numbers.append(int(input()))

max_num = max(numbers)

dp = [0 for _ in range(max_num + 1)]

dp[1] = 1
if max_num >= 2:
    dp[2] = 2
if max_num >= 3:
    dp[3] = 4
if max_num >= 4:
    for i in range(4,max_num + 1):
        dp[i] = (dp[i-3] + dp[i-2] + dp[i-1])%1000000009

for i in numbers:
    print(dp[i])