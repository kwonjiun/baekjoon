n, m = map(int,input().split())

numbers = sorted(list(map(int,input().split())))

L = []

def dfs(start:int, index:int):
    global n,m,numbers, L
    if index == m:
        print(*L)
        return
    temp = 0
    for i in range(start,n):
        if numbers[i] != temp:
            L.append(numbers[i])
            temp = numbers[i]
            dfs(i+1,index+1)
            L.pop()


dfs(0,0)

