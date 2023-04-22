import sys

input = sys.stdin.readline

n = int(input())

S = [list(map(int,input().split())) for _ in range(n)]


min_dis = 1000000000

visited = [False] * n

def dfs(index :int):
    global n , visited
    if index == n:
        calcul()
        return

    visited[index] = True
    dfs(index+1)
    visited[index] = False
    dfs(index+1)

def calcul():
    global visited, n, min_dis, S
    cost1, cost2 = 0, 0
    for i in range(n):
        for j in range(n):
            if visited[i] and visited[j]:
                cost1 += S[i][j]
            elif not visited[i]and  not visited[j]:
                cost2 += S[i][j]
    min_dis = min(min_dis, abs(cost1-cost2))
dfs(0)
print(min_dis)