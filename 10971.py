import sys

input = sys.stdin.readline

n = int(input())

W = [list(map(int,input().split())) for _ in range(n)]

min_path = 10000000

L = []

visited = [False] * n

def dfs(index :int):
    global min_path, L, visited, W , n 
    if index == n:
        temp = 0
        for i in range(n):
            x, y = i%n, (i+1)%n
            if W[L[x]][L[y]] == 0:
                return
            else:
                temp += W[L[x]][L[y]]
        min_path = min(min_path, temp)
        return
    for i in range(n):
        if not visited[i]:
            L.append(i)
            visited[i] = True
            dfs(index+1)
            L.pop()
            visited[i] = False
dfs(0)
print(min_path)