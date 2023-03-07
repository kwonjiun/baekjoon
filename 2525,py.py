hour, minute = map(int,input().split())
time = int(input())

total = (hour*60 + minute + time)%(24*60)

print(total//60,total%60)
