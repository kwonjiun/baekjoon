import sys
from collections import deque
input = sys.stdin.readline

N, M, V = map(int,input().split())

relation = [[ ] for _ in range(N + 1)]

for i in range(M):
    a, b = map(int,input().split())
    relation[a].append(b)
    relation[b].append(a)

for i in range(N+1):
    relation[i] = sorted(relation[i])

L1 = []
L2 = []
visited= [False] * (N + 1)

def dfs(v:int):
    if not visited[v]:
        L1.append(v)
        visited[v] = True
        for i in relation[v]:
            dfs(i)
    

def bfs(v :int):
    q = deque([v])
    visited[v] = True

    while q:
        v = q.popleft()
        L2.append(v)
        for i in relation[v]:
            if not visited[i]:
                q.append(i)
                visited[i] = True
    

dfs(V)
print(*L1)
visited= [False] * (N + 1)
bfs(V)
print(*L2)