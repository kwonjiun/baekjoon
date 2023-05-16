import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

rel = [[] for _ in range(n+1)]

for _ in range(n):
    temp = list(map(int,input().split()))
    a = temp[0]
    i = 1
    while temp[i] != -1:
        b = temp[i]
        cost = temp[i+1]
        rel[a].append([b,cost])
        i += 2
    
visited = [-1] * (n+1)
visited[1] = 0
q = deque([1])
max_value = 0
index =0
while q:
    x = q.popleft()
    for y, cost in rel[x]:
        if visited[y] == -1 or visited[y] > visited[x] + cost:
            visited[y] = visited[x] + cost
            if max_value < visited[y]:
                max_value = visited[y]
                index = y
            q.append(y)

visited = [-1] * (n+1)
visited[index] = 0
q = deque([index])
max_value = 0
while q:
    x = q.popleft()
    for y, cost in rel[x]:
        if visited[y] == -1 or visited[y] > visited[x] + cost:
            visited[y] = visited[x] + cost
            if max_value < visited[y]:
                max_value = visited[y]
            q.append(y)
print(max_value)