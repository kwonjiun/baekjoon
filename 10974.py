n = int(input())

L = []

def dfs(index : int):
    if index == n:
        print(*L)
        return
    for i in range(1,n+1):
        if i not in L:
            L.append(i)
            dfs(index+1)
            L.pop()
dfs(0)