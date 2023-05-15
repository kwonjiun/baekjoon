import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

rel = [[] for _ in range(n+1)]

parent = [-1] * (n+1)
parent[1] = 0

for i in range(n-1):
    a, b = map(int,input().split())
    rel[a].append(b)
    rel[b].append(a)


q = deque([1])

while q:
    x = q.popleft()
    for i in rel[x]:
        if parent[i] == -1:
            parent[i] = x
            q.append(i)

for i in parent[2:]:
    print(i)