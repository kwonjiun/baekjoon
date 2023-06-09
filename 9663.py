n = int(input())

answer = 0
L = [0] * n

def promise(x):
    for i in range(x):
        if L[x] == L[i] or abs(L[x] - L[i]) == abs(x-i):
            return False
    return True


def dfs(x: int):
    global answer
    if x == n:
        answer += 1
        return
    else:
        for i in range(n):
            L[x] = i
            if promise(x):
                dfs(x+1)
dfs(0)
print(answer)

