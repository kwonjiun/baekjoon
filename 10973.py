n = int(input())

numbers = list(list(map(int,input().split())))

for i in range(n-2,-1,-1):
    if numbers[i] > numbers[i+1]:
        index = i
        for j in range(n-1,-1,-1):
            if numbers[j] < numbers[index]:
                numbers[index],numbers[j] = numbers[j],numbers[index]
                numbers = numbers[:index+1]+ sorted(numbers[index+1:],reverse=True)
                print(*numbers)
                exit(0)

print(-1)