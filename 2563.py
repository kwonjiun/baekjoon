white = [[0 for i in range(100)] for j in range(100)]

n = int(input())

for i in range(n):
    m,n = map(int,input().split())
    for j in range(m,m+10):
        for l in range(n,n+10):
            white[j][l] = 1
answer = sum([sum(white[i]) for i in range(100)])
print(answer)