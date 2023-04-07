import sys

input = sys.stdin.readline

N, B = map(int,input().split())

answer = ''

while N != 0:
    temp = N % B

    if temp < 10:
        answer =  str(temp) + answer
    else:
        answer = chr(temp+55) + answer
    N //= B
print(answer)