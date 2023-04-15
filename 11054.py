import sys

input = sys.stdin.readline

n = int(input())

numbers = list(map(int,input().split()))
dp = [1 for _ in range(n)]
answer = [1 for _ in range(n)]
for i in range(n):
    for j in range(i):
        if numbers[i] > numbers[j]:
            dp[i] = max(dp[i], dp[j] + 1)
for i in range(n-1):
   for j in range(i+1,n):
       if numbers[j] < numbers[i]:
           dp[j] = max(dp[j], dp[i] + 1)
        
        
print((max(dp)))
            