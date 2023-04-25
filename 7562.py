import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

dx = [-2, -2, -1, -1, 1, 1, 2, 2]
dy = [1, -1, 2, -2 ,2 , -2, 1 ,-1]

for i in range(n):
    l = int(input())
    x, y = map(int,input().split())
    des_x, des_y = map(int,input().split())

    _map = [[0] * l for _ in range(l)]
    _map[x][y] = 1
    q = deque([[x,y]])
    while q:
        x,y = q.popleft()
        for j in range(8):
            next_x = x + dx[j]
            next_y = y + dy[j]
            if 0 <= next_x <l and 0<= next_y < l:
                if _map[next_x][next_y] == 0:
                    q.append([next_x,next_y])
                    _map[next_x][next_y] = _map[x][y] + 1
        
    
    print(_map[des_x][des_y] -1)
