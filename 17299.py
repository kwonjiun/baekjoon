import sys
from collections import Counter

input = sys.stdin.readline

n = int(input())

numbers = list(map(int,input().split()))

counts = Counter(numbers)

stack= []

answer = [-1 for i in range(n)]

for i in range(n):
    while stack and counts[numbers[stack[-1]]] < counts[numbers[i]]:
        answer[stack.pop()] = numbers[i]
    stack.append(i)

print(*answer)