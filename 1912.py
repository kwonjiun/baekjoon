import sys 

input = sys.stdin.readline

n = int(input())

numbers = list(map(int,input().split()))

dp = [i for i in numbers]

for i in range(1,n):
    temp = dp[i-1] + numbers[i]
    if temp > 0 and numbers[i] < temp:
        dp[i] = temp
print(max(dp))