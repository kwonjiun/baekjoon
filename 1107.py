channel= int(input())

n = int(input())

if n == 0:
    print(min(abs(channel-100), len(str(channel))))
else:
    broke = list(input().rstrip().split())

    min_try = abs(channel-100)

    for i in range(1000001):
        possible = True
        for j in range(n):
            if broke[j] in list(str(i)):
                possible = False
                break
        if possible:
            min_try = min(min_try,len(str(i)) + abs(channel -i))
        i += 1
    print(min_try)
