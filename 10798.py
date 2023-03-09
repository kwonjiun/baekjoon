words = [[-1 for i in range(15)] for j in range(5)]

for i in range(5):
    temp = list(input())
    words[i][:len(temp)] = temp

for i in range(15):
    for j in range(5):
        if words[j][i] != -1:
            print(words[j][i],end = '')
