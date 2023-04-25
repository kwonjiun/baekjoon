import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

_map = [list(map(int,input().rstrip())) for _ in range(n)]

visited = [[False]*n for _ in range(n)]
complex = []


def is_in(x:int, y:int):
    global n
    return 0 <= x <= n-1 and 0 <= y <= n-1

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            
            if _map[i][j] == 0:
                visited[i][j] = True
                
            else:
                count = 0
                q = deque([[i,j]])
                while q:
                    x, y = q.popleft()
                    if not visited[x][y]:
                        visited[x][y] = True
                        if _map[x][y] == 1:
                            count +=1
                            if is_in(x,y-1):
                                q.append([x,y-1])
                            if is_in(x,y+1):
                                q.append([x,y+1])
                            if is_in(x-1,y):
                                q.append([x-1,y])
                            if is_in(x+1,y):
                                q.append([x+1,y])
                complex.append(count)
                        
complex.sort()
print(len(complex))
for i in complex:
    print(i)
                    


