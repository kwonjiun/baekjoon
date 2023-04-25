import sys
from collections import deque
input = sys.stdin.readline

index = [[0,1],[1,0],[-1,0],[0,-1],[1,1],[1,-1],[-1,1],[-1,-1]]

while True:


    n , m = map(int,input().split())

    if n == 0 or m == 0:
        break
    
    _map = [list(map(int,input().split())) for _ in range(m)]

    count = 0
    for i in range(m):
        for j in range(n):
            if _map[i][j] == 1:
                count += 1
                q = deque([[i,j]])
                while q:
                    x,y = q.popleft()
                    if _map[x][y] == 1:
                        _map[x][y] = 0
                        for k in index:
                            if 0 <= x+k[0] <m and 0<= y + k[1] < n:
                                q.append([x+k[0], y+k[1]])

    print(count)

