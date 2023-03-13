import sys

input = sys.stdin.readline

n, k = map(int, input().split())

people =list(range(1,n+1))

num = 0
answer = []
for i in range(len(people)):
    num = (num + k - 1)%len(people)
    print(people[num])
    answer.append(str(people.pop(num)))


print("<", ", ".join(answer), ">", sep = "")
    
    
