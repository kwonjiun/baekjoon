import sys
from collections import deque

input = sys.stdin.readline

m,n = map(int,input().split())

_map = [list(map(int,input().rstrip())) for _ in range(n)]

q = deque([[0,0]])

dx = [1,0,-1,0]
dy = [0,1,0,-1]

visited = [[sys.maxsize]*m for _ in range(n)]
visited[0][0] = 0

while q:
    x,y = q.popleft()

    for i in range(4):
        n_x = x + dx[i]
        n_y = y + dy[i]
        if 0 <= n_x < n and 0 <= n_y < m:
            if _map[n_x][n_y] == 1 and visited[n_x][n_y] > visited[x][y] + 1:
                visited[n_x][n_y] =  visited[x][y]+ 1
                q.append([n_x,n_y])
            elif _map[n_x][n_y] == 0 and visited[n_x][n_y] > visited[x][y]:
                visited[n_x][n_y] =  visited[x][y]
                q.append([n_x,n_y])
print(visited[n-1][m-1])
