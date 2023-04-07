import sys

input = sys.stdin.readline

notation = list(input().rstrip())

oper = []

answer = ''

for i in notation:
    if i.isalpha():
        answer += i
    elif i == '(':
        oper.append('(')
    elif i == '*' or i == '/':
        while oper and (oper[-1] == '*' or oper[-1] == '/') and (oper[-1] != '('):
            answer += oper.pop()
        oper.append(i)
    elif i == '+' or i == '-' :
        while oper and oper[-1] != '(':
            answer += oper.pop() 
        oper.append(i)
    elif i == ')' :
        while oper and oper[-1] != '(':
            answer += oper.pop()
        oper.pop()
        
while oper:
    answer += oper.pop()


print(answer)    


