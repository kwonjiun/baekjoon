import sys

def fact(n: int):
    answer = 1
    while n!= 0:
        answer*=n
        n -= 1
    return answer
input = sys.stdin.readline

number = list(str(fact(int(input()))))
count = 0


while number.pop() == '0':
    count+=1


print(count)