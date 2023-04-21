n,m = map(int,input().split())

L = []

def dfs(start:int ,index:int):
    if index == m:
        print(*L)
        return
    
    for i in range(start,n+1):
        L.append(i)
        dfs(i,index+1)
        L.pop()

dfs(1,0)