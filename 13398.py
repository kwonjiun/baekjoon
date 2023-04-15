import sys

input =sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

dp1 = [0 for _ in range(n)]
dp2 = [0 for _ in range(n)]

dp1[0] = a[0]
dp2[0] = -1000

for i in range(1, n):
    dp1[i] = max(a[i], a[i]+dp1[i-1])
    dp2[i] = max(dp1[i-1], dp2[i-1]+a[i])


print(max(dp1+dp2))