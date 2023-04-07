import sys

n = int(sys.stdin.readline())

answer = ''
if n == 0:
    print(0)
else:
    while n != 0:
        if n%-2:
            answer ='1' + answer
            n = n//-2 + 1
        else:
            answer = '0' + answer
            n = (n//-2)  
    print(answer)