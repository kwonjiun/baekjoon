n, m = map(int,input().split())

numbers = sorted(list(map(int,input().split())))

L = []

def dfs(index:int):
    global n , m , L , numbers
    if index == m :
        print(*L)
        return
    
    for i in range(n):
        L.append(numbers[i])
        dfs(index+1)
        L.pop()

dfs(0)