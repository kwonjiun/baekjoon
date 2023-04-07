import sys

n = int(sys.stdin.readline())

numbers = [int(sys.stdin.readline()) for _ in range(n)]
max_num = max(numbers)


answer = [0 for _ in range(max_num+1)]

if max_num == 1:
    answer[1] = 1
elif max_num==2:
    answer[1] = 1
    answer[2] = 2
else:
    answer[1] = 1
    answer[2] = 2
    answer[3] = 4

    for i in range(4,max_num+1):
        answer[i] = answer[i-1] + answer[i-2] + answer[i-3]

for i in range(n):
    print(answer[numbers[i]])