import sys

input = sys.stdin.readline

N, M = map(int,input().split())

S = [list(map(int,input().rstrip())) for _ in range(N)]


answer = 0

for i in range(1<<N*M):
    total = 0
    for row in range(N):
        temp = 0
        for col in range(M):
            index = row *M + col
            if i & ( 1 << index) != 0:
                temp = temp*10 + S[row][col]
            else: 
                total += temp
                temp = 0
        total += temp
    for col in range(M):
        temp = 0
        for row in range(N):
            index = row*M + col
            if i & ( 1 << index) == 0:
                temp = temp*10 + S[row][col]
            else:
                total += temp
                temp = 0
        total += temp
    answer = max(answer, total)
print(answer)


