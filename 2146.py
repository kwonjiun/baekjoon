import sys 
from collections import deque
sys.setrecursionlimit(10**9)

input = sys.stdin.readline

n = int(input())

M = [list(map(int,input().split())) for _ in range(n)]

dx = [1,0,-1,0]
dy = [0,1,0,-1]

sector = 2
answer = sys.maxsize

def spread(x,y, sector):
    for i in range(4):
        n_x = x + dx[i]
        n_y = y + dy[i]
        if 0<= n_x < n and 0 <= n_y < n and M[n_x][n_y] == 1:
            M[n_x][n_y] = sector
            spread(n_x,n_y,sector)

def find(sector):
    global answer
    q = deque()
    distance = [[-1]*n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if M[i][j] == sector:
                q.append([i,j])
                distance[i][j] = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            n_x = x + dx[i]
            n_y = y + dy[i]
            if 0<= n_x < n and 0 <= n_y < n:
                if M[n_x][n_y] != 0 and M[n_x][n_y] != sector:
                    answer = min(answer, distance[x][y] )
                    return
                elif M[n_x][n_y] == 0 and distance[n_x][n_y] == -1:
                    distance[n_x][n_y] = distance[x][y] + 1
                    q.append([n_x,n_y])
            
for i in range(n):
    for j in range(n):
        if M[i][j] == 1:
            M[i][j] = sector
            spread(i,j,sector)
            sector += 1

for  a in range(2,sector):
    find(a)

        
print(answer)

            