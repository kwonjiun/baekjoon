import sys

input = sys.stdin.readline

n = int(input())

L = list(map(int,input().split()))

ADD,SUB,MUL,DIV = map(int,input().split())

max_number = -10e9
min_number = 10e9


def c_divide(a:int, b:int):
    if a > 0 :
        return a//b
    else:
        return -(-a // b)
    
def dfs(index:int, sum:int, ADD:int,SUB:int,MUL:int,DIV:int):
    global max_number, min_number
    if index == n-1:
        if sum < min_number:
            min_number = sum
        if sum > max_number:
            max_number = sum
        return
    else:
        if ADD > 0:
            dfs(index+1, sum + L[index+1], ADD-1,SUB,MUL,DIV)
        if SUB > 0:
            dfs(index+1, sum - L[index+1], ADD,SUB-1,MUL,DIV)
        if MUL > 0:
            dfs(index+1, sum * L[index+1], ADD,SUB,MUL-1,DIV)
        if DIV > 0:
            dfs(index+1, c_divide(sum , L[index+1]), ADD,SUB,MUL,DIV-1)
dfs(0,L[0],ADD,SUB,MUL,DIV)
print(max_number)
print(min_number)