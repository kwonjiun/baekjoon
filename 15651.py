n , m = map(int,input().split())

L = []

def dfs(index:int):
    if index == m:
        print(*L)
        return
    
    for i in range(1,n+1):
        L.append(i)
        dfs(index+1)
        L.pop()

dfs(0)