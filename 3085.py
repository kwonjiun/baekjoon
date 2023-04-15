import sys

input = sys.stdin.readline

n = int(input())

temp = [list(input().rstrip()) for _ in range(n)]


def find(candies:list,n:int):
    max_candy = 0
    
    for i in range(n):
        dp = [1]*n
        for j in range(1,n):
            if candies[i][j-1] == candies[i][j]:
                dp[j] = dp[j-1]+1
        max_candy = max(max_candy,max(dp))
    
    candies = list(map(list,zip(*candies)))
    
    for i in range(n):
        dp = [1]*n
        for j in range(1,n):
            if candies[i][j-1] == candies[i][j]:
                dp[j] = dp[j-1]+1
        max_candy = max(max_candy,max(dp))
    return max_candy

def change(candies:list,n:int):
    max_candies = 0
    for i in range(n):
        for j in range(n-1):
            candies[i][j],candies[i][j+1] = candies[i][j+1],candies[i][j]
            max_candies = max(max_candies,find(candies,n))
            candies[i][j],candies[i][j+1] = candies[i][j+1],candies[i][j]

    for i in range(n-1):
        for j in range(n):
            candies[i][j],candies[i+1][j] = candies[i+1][j],candies[i][j]
            max_candies = max(max_candies,find(candies,n))
            candies[i][j],candies[i+1][j] = candies[i+1][j],candies[i][j]
    return max_candies



print(change(temp,n))