import sys

m, n = map(int,input().split())

_map = [list(map(int,input().split())) for _ in range(n)]
dx = [0,1,0,-1]
dy = [1,0,-1,0]


q = []

for i in range(n):
    for j in range(m):
        if _map[i][j] == 1:
            q.append([i,j])

count = 0
while True:
    temp = []
    for i in q:
        x,y = i
        for i in range(4):
            next_x = x + dx[i]
            next_y = y + dy[i]
            if 0 <= next_x < n and 0 <= next_y < m:
                if _map[next_x][next_y] == 0:
                    temp.append([next_x,next_y])
                    _map[next_x][next_y] = 1
    q = temp.copy()
    if q:
        count+= 1
    else:
        break

for i in range(n):
    for j in range(m):
        if _map[i][j] == 0:
            print(-1)
            exit()

print(count)
        
