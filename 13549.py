from collections import deque

n, k = map(int,input().split())

if n > k:
    print(n-k)
    exit()
visited = [-1] * 100001

visited[n] = 0

q = deque([n])

while q:
    now = q.popleft()

    if now == k:
        print(visited[now])
        break
    if 2 * now <= 100000 and visited[2*now] == -1 :
        visited[2*now] = visited[now]
        q.appendleft(2*now)
    if now+ 1 <= 100000 and visited[now+1] == -1:
        visited[now+1] = visited[now] + 1
        q.append(now+1)
    if now-1 >= 0 and visited[now-1] == -1:
        visited[now-1] = visited[now] + 1
        q.append(now-1)
    