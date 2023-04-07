import sys

input = sys.stdin.readline

n = int(input())

numbers = [int(input()) for i in range(n)]

max_num =max(numbers)

prime = [True for i in range(max_num + 1)]

prime[0], prime[1] = False, False

for i in range(2, int(max_num ** 0.5) + 1):
    if prime[i]:
        for j in range(2*i, max_num+1, i):
            prime[j] = False

def howmany(n :int):
    a,b = 0, 0
    if n % 2 == 0:
        a, b = n//2, n//2
    else:
        a, b = n//2, n//2+1
    
    count = 0

    while a != 1:
        if prime[a] and prime[b]:
            count+=1
        a -= 1
        b += 1
    return count

for i in range(n):
    print(howmany(numbers[i]))
