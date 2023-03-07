hour, minute = map(int,input().split())

total = hour*60 + minute -45

if(total < 0):
    total += 60*24

print(total//60, total%60)