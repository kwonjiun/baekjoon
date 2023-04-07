import sys

input = sys.stdin.readline

def gcd(a:int, b: int):


    if b == 0:
        return a
    else:
        return gcd(b,a%b)
N, S = map(int,input().split())

bro = list(map(int,input().split()))

distance = [i-S for i in bro]

answer = distance[0]
for i in range(1, len(distance)):
    answer = gcd(answer,distance[i])
    if answer == 1:
        break
print(abs(answer))

