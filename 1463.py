import sys

n = int(sys.stdin.readline())

if n == 1:
    print(0)
elif n < 4 :
    print(1)
else:
    count = 0

    temp = [0 for _ in range(n+1)]

    temp[1],temp[2],temp[3] = 1,1,1

    for i in range(4,n+1):
        if i % 6 == 0:
            temp[i] = min(temp[i//3]+1, temp[i//2]+1, temp[i-1]+1)
        elif i%3 == 0:
            temp[i] = min(temp[i//3]+1, temp[i-1]+1)
        elif i%2== 0:
            temp[i] = min(temp[i//2]+1, temp[i-1]+1)
        else:
            temp[i] = temp[i-1] + 1
    print(temp[-1])