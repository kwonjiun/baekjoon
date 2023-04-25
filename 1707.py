import sys
sys.setrecursionlimit(10 ** 6)

input = sys.stdin.readline


n = int(input())

for i in range(n):
    V, E = map(int,input().split())
    relation = [[] for _ in range(V+1)]
    visited = [False] * ( V + 1 )
    what_group = [0] * ( V + 1 )
    answer = 'YES'
    for j in range(E):
        a,b = map(int,input().split())
        relation[a].append(b)
        relation[b].append(a)
    
    def dfs(v: int ,group:int):
        global V,E,relation,visited,what_group,answer

        if visited[v]:
            if group != what_group[v]:
                answer = 'NO'
                return
        else:
            visited[v] = True
            what_group[v] = group
            for i in relation[v]:
                dfs(i,-group)
    for k in range(1,V+1):
        if not visited[k]:
            dfs(k,1)

    print(answer)
    
        
