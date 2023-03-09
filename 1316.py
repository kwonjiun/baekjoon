n = int(input())

numbers = 0
for i in range(n):
    temp = input()
    error = 0
    for j in range(len(temp)-1):
        if temp[j] == temp[j+1]:
            pass
        elif temp[j] in temp[j+1:]:
            error = 1
            break
    if error == 0:
        numbers += 1

print(numbers)

