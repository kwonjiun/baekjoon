import sys

input = sys.stdin.readline

n = int(input())

A = input().rstrip().split()

answer = []

L = []

def dfs(index:int):
    if index == n+1:
        for i in range(n):
            if A[i] == '<':
                if not L[i] < L[i+1]:
                    return
            elif A[i] == '>':
                if not L[i] > L[i+1]:
                    return
        answer.append(''.join(map(str,L)))
        return
    for i in range(10):
        if i not in L:
            L.append(i)
            dfs(index+1)
            L.pop()
            
dfs(0)

print(max(answer))
print(min(answer))
