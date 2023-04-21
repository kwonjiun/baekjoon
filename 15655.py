n, m = map(int,input().split())

numbers = sorted(list(map(int,input().split())))
L = []

def dfs(start:int, index:int):
    global n, m , numbers, L
    if index == m :
        print(*L)
        return
    for i in range(start,n):
        L.append(numbers[i])
        dfs(i+1,index+1)
        L.pop()
dfs(0,0)