import sys

input = sys.stdin.readline

N, M = map(int,input().split())

relation = [[] for _ in range(N+1)]

visited = [False] * (N+1)

for i in range(M):
    a, b = map(int,input().split())
    relation[a].append(b)
    relation[b].append(a)



def dfs(v:int):
    visited[v] = True
    for i in relation[v]:
        if not visited[i]:
            dfs(i)
            
answer = 0

for i in range(1,N+1):  
    if not visited[i]:
        if not relation[i]:
            answer += 1
            visited[i] = True
        else:
            dfs(i)
            answer += 1
            
print(answer)