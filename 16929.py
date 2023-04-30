import sys

input = sys.stdin.readline

n,m = map(int,input().split())

_map = [list(input().rstrip()) for _ in range(n)]


dx = [0, 1 , 0, -1]
dy = [1, 0, -1, 0]
visited = [[False] * m for _ in range(n)]

def dfs(x,y, start_x, start_y, cnt):
    global _map , visited, dx, dy , n , m

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0<=nx<n and 0<=ny<m:
            if cnt >= 4 and start_x == nx and start_y == ny:
                print('Yes')
                exit()
            if _map[start_x][start_y] == _map[nx][ny] and not visited[nx][ny]:
                visited[nx][ny] = True
                dfs(nx,ny,start_x,start_y,cnt+1)
                visited[nx][ny] = False

for i in range(n):
    for j in range(m):
        visited[i][j] = True
        dfs(i,j,i,j,1)
print("No")