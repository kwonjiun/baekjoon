import sys

input = sys.stdin.readline

L, C = map(int,input().split())

alpha = sorted(input().split())

code = []

vo = 0

con = 0


def dfs(start:int ,index :int):
    global L,C,alpha,code, vo, con
    if index == L and vo >= 1 and con >= 2:
        print(''.join(code))
    
    for i in range(start,C):
        if alpha[i] not in code:
            if alpha[i] in ['a','e','i','o','u']:
                vo +=1
                code.append(alpha[i])
                dfs(i+1,index+1)
                code.pop()
                vo -=1
            else:
                con +=1
                code.append(alpha[i])
                dfs(i+1, index+1)
                code.pop()
                con -=1
dfs(0, 0)

    