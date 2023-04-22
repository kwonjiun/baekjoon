import sys

input = sys.stdin.readline

n = int(input())

T, P = [], []

for i in range(n):
    Ti, Pi, = map(int,input().split())
    T.append(Ti)
    P.append(Pi)


max_cost = 0
cost = 0
def dfs(date : int):
    global n, T, P,cost,max_cost
    if date <= n:
        max_cost = max(max_cost,cost)
    for i in range(date,n):
        if i+T[i] <= n:
            date = i + T[i]
            cost += P[i]
            dfs(date)
            date = i
            cost -= P[i]
        
            
dfs(0)
print(max_cost)

