import sys

input = sys.stdin.readline

def solution(list:list):
    sum_list = sum(list)
    for i in range(8):
        for j in range(i+1,9):
            if sum_list-list[i]-list[j] == 100:
                return i ,j
            
list = [int(input()) for _ in range(9)]
i,j = solution(list)
a,b = list[i],list[j]
list.remove(a)
list.remove(b)

for i in sorted(list):
    print(i)

