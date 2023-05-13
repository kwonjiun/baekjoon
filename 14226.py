from collections import deque

n = int(input())

q = deque([[1,0]])
visited = [[-1] * 1001 for _ in range(1001)]
visited[1][0] = 0
while q:
    s, c = q.popleft()
    if s+c == n :
        print(visited[s][c] + 1)
        break
    if s+c <= 1000 and visited[s+c][c] == -1:
        visited[s+c][c] = visited[s][c] + 1
        q.append([s+c,c])
    if visited[s][s] == -1:
        visited[s][s] = visited[s][c] + 1
        q.append([s,s])
    if s > 0 and visited[s-c][c] == -1:
        visited[s-1][c] = visited[s][c] + 1
        q.append([s-1,c])