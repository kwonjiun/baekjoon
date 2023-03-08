m, n = map(int,input().split())

backets = list(range(1,m+1))

for a in range(n):
    i , j = map(int, input().split())
    backets[i-1:j] = list(reversed(backets[i-1:j]))
    
print(*backets)
