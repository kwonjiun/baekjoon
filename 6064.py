import sys

input = sys.stdin.readline

n = int(input())

for i in range(n):
    M,N,x,y = map(int,input().split())
    possible = True
    k = x
    while k <= M*N:
        if (k-x)%M == 0 and (k-y)%N == 0:
            break
        k += M

    if k <= M*N:
        print(k)
    else:
        print(-1)
