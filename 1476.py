e,s,m = map(int,input().split())

a,b,c = 0,0,0
i = 0
while True:
    if e-1 == a and s-1 == b and m-1 == c:
        print(i+1)
        break
    i+=1
    a = (a+1)%15
    b = (b+1)%28
    c = (c+1)%19
    
