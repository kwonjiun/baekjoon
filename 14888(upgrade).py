import sys

input = sys.stdin.readline

n = int(input())

numbers = list(map(int,input().split()))

ADD, SUB, MUL, DIV = map(int, input().split())

max_value = - (10 ** 9)
min_value =  10 ** 9

def devide(a, b ):
    if a >= 0 :
        return a // b
    else:
        return -(-a // b)

def dfs(index, values , ADD, SUB, MUL, DIV):
    global max_value, min_value
    if index ==n -1 :
        if values > max_value:
            max_value = values
        if values < min_value:
            min_value = values
        return
    else:
        if ADD > 0:
            dfs(index+1, values + numbers[index+1], ADD-1, SUB, MUL, DIV)
        if SUB > 0:
            dfs(index+1, values - numbers[index+1], ADD, SUB-1, MUL, DIV)
        if MUL > 0:
            dfs(index+1, values * numbers[index+1], ADD, SUB, MUL-1, DIV)
        if DIV > 0:
            dfs(index+1, devide(values, numbers[index+1]), ADD, SUB, MUL, DIV-1)
    
dfs(0,numbers[0],ADD,SUB,MUL,DIV)
print(max_value)
print(min_value)
