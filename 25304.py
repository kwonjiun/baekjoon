pay = int(input())

many = int(input())

total = 0 

for i in range(many):
    cost, number = map(int,input().split())
    total += cost*number

if(pay == total):
    print("Yes")
else:
    print("No")