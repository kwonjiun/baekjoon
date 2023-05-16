import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())

rel = [[] for _ in range(n+1)]

for i in range(n-1):
    a, b, cost = map(int,input().split())
    rel[a].append([b,cost])

answer = 0

def dfs(n, d):
    max1, max2 = 0, 0
    for i in rel[n]:
        temp_max = dfs(i[0], i[1])
        if max1 >= max2:
            max2 = max(max2, temp_max)
        else:
            max1 = max(max1, temp_max)
    global answer
    answer = max(answer, max1+max2)
    return max(max1+d, max2+d)

dfs(1,0)
print(answer)

