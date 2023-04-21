import sys 

input = sys.stdin.readline

L = []
def dfs(start: int, index: int, n:int, numbers:list):
    global L
    if index == 6:
        print(*L)
        return
    for i in range(start, n):
        L.append(numbers[i])
        dfs(i+1, index+1,n,numbers)
        L.pop()

while True:
    temp = list(map(int,input().split()))
    if temp[0] == 0:
        exit(0)
    else:
        n, numbers = temp[0], temp[1:]
        dfs(0,0,n,numbers)
        print()
