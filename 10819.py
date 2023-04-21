n = int(input())

numbers = list(map(int,input().split()))

L = []
visited = [False] * n
answer = 0

def dfs(index:int):

    global n , numbers, L, answer

    if index == n :
        temp = 0
        for a in range(n-1):
            temp += abs(L[a] - L[a+1])
        answer = max(answer, temp)
        return
    for i in range(n):
        if not visited[i]:
            L.append(numbers[i])
            visited[i] = True
            dfs(index+1)
            L.pop()
            visited[i] = False


dfs(0)
print(answer)
