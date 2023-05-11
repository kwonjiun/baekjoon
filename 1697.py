from collections import deque

x, y = map(int,input().split())

distance = [0] * 100001

q = deque()

q.append(x)

while q:
    a = q.popleft()
    if a == y:
        break
    for next in (a -1, a + 1 , 2* a):
        if 0 <= next <= 100000 and not distance[next]:
            distance[next] = distance[a] + 1
            q.append(next)
    
   

print(distance[y])

