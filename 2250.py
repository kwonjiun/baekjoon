import sys

input = sys.stdin.readline

n = int(input())

rel = [[] for _ in range(n+1)]
root = [1] * (n+1)
root[0] = 0

for i in range(1, n+1):
    node , left, right = list(map(int,input().split()))
    rel[node] = [left, right]
    if left != -1: root[left] = 0
    if right != -1: root[right] = 0


answer = [[]for _ in range(n+1)]
index = 1

def post(n, level):
    left, right = rel[n]
    if left != -1:
        post(left, level+1)
    global index
    answer[level].append(index)
    index += 1
    if right != -1:
        post(right, level+1)

post(root.index(1),1)

level = 1
max_value = max(answer[1]) - min(answer[1]) + 1

for i in range(2,n+1):
    if not answer[i]: break
    if max_value < max(answer[i]) - min(answer[i]) + 1:
        max_value =  max(answer[i]) - min(answer[i]) + 1
        level = i

print(level, max_value)
