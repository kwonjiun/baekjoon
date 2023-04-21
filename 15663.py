n, m = map(int,input().split())

numbers = sorted(list(map(int,input().split())))

L = []

visited = []
def dfs(index:int):
    global n,m,numbers, L,visited
    if index == m:
        print(*L)
        return
    temp = 0
    for i in range(n):
        if i not in visited and numbers[i] != temp:
            visited.append(i)
            L.append(numbers[i])
            temp = numbers[i]
            dfs(index+1)
            L.pop()
            visited.pop()

dfs(0)

