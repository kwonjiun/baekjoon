import sys
input = sys.stdin.readline

count = 0

string = input()

pieces = 0

for i in range(len(string)):
    if(string[i] == "("):
        count += 1
    if(string[i] == ")"):
        if string[i-1] == "(":
            count -= 1
            pieces += count
        else:
            count -= 1
            pieces += 1


            
print(pieces)
