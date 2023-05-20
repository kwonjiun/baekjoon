import sys

input = sys.stdin.readline

n = int(input())

words = [input().rstrip() for _ in range(n)]

select = {}

for i in range(n):
    for j in range(len(words[i])):
        if words[i][j] in select:
            select[words[i][j]] += 10 ** (len(words[i]) - j - 1)
        else:
            select[words[i][j]] = 10 ** (len(words[i]) - j - 1)

numbers = [i for i in select.values()]

numbers.sort(reverse=True)

answer = 0
pow = 9

for i in numbers:
    answer += i*pow
    pow -= 1
print(answer)

