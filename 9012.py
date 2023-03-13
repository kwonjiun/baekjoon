import sys

n = int(sys.stdin.readline())



for i in range(n):
    temp = sys.stdin.readline()
    error = 0
    for j in range(len(temp)):
        if temp[j] == '(':
            error += 1
        elif temp[j] == ')':
            error -= 1
        
        if error < 0:
            break
    if error == 0:
        print("YES" )
    else:
        print("NO" )