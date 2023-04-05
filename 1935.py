import sys

input = sys.stdin.readline

n = int(input())

string = input().rstrip()

answer = []

numbers = [float(input()) for i in range(n)]

for i in range(len(string)):
    if string[i] == "*" or string[i] == "+" or string[i] == "-" or string[i] == "/" :
        if string[i] == "*":
            b = answer.pop()
            a = answer.pop()
            answer.append(a*b)
        if string[i] == "+":
            b = answer.pop()
            a = answer.pop()
            answer.append(a+b)
        if string[i] == "-":
            b = answer.pop()
            a = answer.pop()
            answer.append(a-b)
        if string[i] == "/":
            b = answer.pop()
            a = answer.pop()
            answer.append(a/b)
    else:
        index = ord(string[i])- 65
        answer.append(numbers[index])
print("{:.2f}".format(answer.pop()))
        
