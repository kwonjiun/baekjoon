import sys

input = sys.stdin.readline

n = int(input())

numbers = list(map(int,input().split()))

stack= []

answer = [-1 for i in range(n)]

for i in range(n):
    while stack and numbers[stack[-1]] < numbers[i]:
        answer[stack.pop()] = numbers[i]
    stack.append(i)
print(*answer)