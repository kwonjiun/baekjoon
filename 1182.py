import sys

N, S = map(int,input().split())

A = list(map(int,input().split()))

visited = [False] * N

count = 0


def dfs(index : int):
    global N,S,A,visited,count
    if index == N:
        temp = 0
        for i in range(N):
            if visited[i]:
                temp += A[i]
        if temp == S:
            count += 1
        return
    visited[index] = True
    dfs(index+1)
    visited[index] = False
    dfs(index+1)

dfs(0)
if S == 0:
    count -= 1
print(count)