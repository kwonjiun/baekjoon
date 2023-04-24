import sys

input = sys.stdin.readline

N,  M = map(int,input().split())

relation = [[] for _ in range(N)]

visited = [False] * N

for i in range(M):
    a, b, = map(int,input().split())
    relation[a].append(b)
    relation[b].append(a)


depth = 0
exist = 0
def dfs(index :int):
    global depth, exist, visited, relation
    if depth >= 5:
        return
    if not visited[index]:
        visited[index] = True
        depth += 1
        if depth == 5:
            exist = 1
            return
        for i in relation[index]:
            dfs(i)
        depth -= 1
        visited[index] = False

for i in range(N):
    dfs(i)
    if exist:
        break
print(exist)