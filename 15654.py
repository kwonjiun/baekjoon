n, m = map(int,input().split())

numbers = sorted(list(map(int,input().split())))

L = []

def dfs( index:int):
    global n, m ,numbers, L
    if index ==m:
        print(*L)
        return
    for i in range(n):
        if numbers[i] not in L:
            L.append(numbers[i])
            dfs(index+1)
            L.pop()

dfs(0)
