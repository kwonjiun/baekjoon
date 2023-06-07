import sys

input = sys.stdin.readline

n = int(input())

L = list(map(int,input().split()))

visited = [0] * 2000000
visited[0]  = 1


def dfs(index:int, sum: int):
    if index == n :
        return
    else:
        dfs(index+1, sum + L[index])
        visited[sum + L[index]] = 1
        dfs(index+1, sum)
        visited[sum] = 1
dfs(0,0)
print(visited.index(0))
