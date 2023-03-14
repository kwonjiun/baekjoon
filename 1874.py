import sys

n = int(sys.stdin.readline())

temp = []

result = []

count = 1

error = True

for i in range(n):
    x = int(sys.stdin.readline())

    while count <= x:
        result.append('+')
        temp.append(count)
        count += 1
        
    if temp[-1] == x:
        result.append('-')
        temp.pop()
    else:
        error = False
        

if not error:
    print("No")
else:
    print('\n'.join(result))
