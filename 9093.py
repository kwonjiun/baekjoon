import sys

n = int(sys.stdin.readline())

for i in range(n):
    temp = sys.stdin.readline().split()
    for j in range(len(temp)):
        print(temp[j][::-1],end = ' ')
    print()