import sys; input = sys.stdin.readline

n =  int(input())
L = list(map(int,input().split()))

answer = 0

def dfs(energy:int):
    global answer
    if len(L) == 2:
        answer = max(answer, energy)
        return
    else:
        for i in range(1, len(L)-1):

            temp_energy = L[i-1] * L[i+1]
            temp = L.pop(i)
            dfs(energy + temp_energy)
            L.insert(i,temp)
dfs(0)

print(answer)