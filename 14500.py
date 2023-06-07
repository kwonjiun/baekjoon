import sys

input = sys.stdin.readline

N, M = map(int,input().split())

_map = [list(map(int, input().split())) for _ in range(N)]

visited = [[False] * M for _ in range(N)]

dx = [0, 1, 0, -1]
dy = [1, 0 ,-1, 0]

answer = 0

def dfs(count : int, sum : int, x:int, y:int):
    global answer

    if count == 4:
        if answer < sum:
            answer = sum
        return
    else:
        for i in range(4):
            n_x = x + dx[i]
            n_y = y + dy[i]
            if 0 <= n_x < N and 0 <= n_y < M and not visited[n_x][n_y]:
                visited[n_x][n_y] = True
                dfs(count+1, sum + _map[n_x][n_y], n_x, n_y)
                visited[n_x][n_y] = False

def exc(x:int,y:int):
    global answer
    
    for i in range(4):
        temp = _map[x][y]
        for j in range(4):
            if i == j:
                pass
            else:
                n_x = x + dx[j]
                n_y = y + dy[j]
                if 0 <= n_x < N and 0 <= n_y < M:
                    temp += _map[n_x][n_y]
                else:
                    temp = 0
                    break
        answer = max(answer, temp)


for i in range(N):
    for j in range(M):
        visited[i][j] = True
        dfs(1,_map[i][j], i,j)
        visited[i][j] = False
        exc(i,j)
print(answer)