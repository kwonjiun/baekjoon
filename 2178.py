import sys
from collections import deque
n, m = map(int,input().split())

_map = [list(map(int,input().rstrip())) for _ in range(n)]
dx = [0,1,0,-1]
dy = [1,0,-1,0]

q = deque([[0,0]])

while q:
    x,y = q.popleft()
    for i in range(4):
        next_x = x + dx[i]
        next_y = y + dy[i]
        if 0 <= next_x < n and 0 <= next_y < m:
            if _map[next_x][next_y] == 1:
                q.append([next_x,next_y])
                _map[next_x][next_y] = _map[x][y] + 1
print(_map[n-1][m-1])
        
