import sys; input = sys.stdin.readline
from collections import deque

n,m = map(int,input().split())

_map = [list(input().strip()) for _ in range(n)]
dx = [0,1,0,-1]
dy = [1,0,-1,0]

position = deque()
temp = []
for i in range(n):
    for j in range(m):
        if _map[i][j] == 'o':
            temp.append(i)
            temp.append(j)

position.append((temp[0],temp[1],temp[2],temp[3], 0 ))

while position:
    x1,y1,x2,y2, cnt = position.popleft()

    if cnt  >= 10:
        print(-1)
        exit()

    for i in range(4):
        nx1,ny1,nx2,ny2 = x1 + dx[i], y1 + dy[i], x2 + dx[i], y2 + dy[i]
        if  0 <= nx1 < n and 0 <= ny1 < m and 0 <= nx2 < n and 0 <= ny2 < m:
            if _map[nx1][ny1] == '#':
                nx1, ny1 = x1, y1
            if _map[nx2][ny2] == '#':
                nx2, ny2 = x2, y2
            position.append((nx1,ny1,nx2,ny2,cnt+1))
        elif not(0 <= nx1 < n and 0 <= ny1 < m) and (0 <= nx2 < n and 0 <= ny2 < m):
            print(cnt + 1)
            exit()
        elif not(0 <= nx2 < n and 0 <= ny2 < m) and (0 <= nx1 < n and 0 <= ny1 < m):
            print(cnt + 1)
            exit()
        else:
            continue

print(-1)
