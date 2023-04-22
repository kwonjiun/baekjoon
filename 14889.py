import sys

input = sys.stdin.readline

n = int(input())

S = [list(map(int,input().split())) for _ in range(n)]

L = []
min_dis = 1000000000
def dfs(start:int, index :int):
    global n , S, L, min_dis
    if index == n//2:
        cost1, cost2 = 0,0
        for i in range(n):
            for j in range(n):
                if i in L and j in L:
                    cost1 += S[i][j]
                elif i not in L and j not in L:
                    cost2 += S[i][j]
        min_dis = min(min_dis,abs(cost1-cost2))
        return
    for i in range(start, n):
        L.append(i)
        dfs(i+1,index+1)
        L.pop()

dfs(0,0)
print(min_dis)