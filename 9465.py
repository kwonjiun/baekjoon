import sys

input = sys.stdin.readline

_ = int(input())

for i in range(_):
    n = int(input())

    cost = []
    cost.append(list(map(int,input().split())))
    cost.append(list(map(int,input().split())))

    cost = list(zip(*cost))
    
    dp = [[0,0,0] for j in range(n)]
    dp[0][0] = cost[0][0]
    dp[0][1] = cost[0][1]

    for j in range(1,n):
        dp[j][0] = max(dp[j-1][1], dp[j-1][2]) + cost[j][0]
        dp[j][1] = max(dp[j-1][0], dp[j-1][2]) + cost[j][1]
        dp[j][2] = max(dp[j-1][0], dp[j-1][1])
    print(max(dp[-1]))
