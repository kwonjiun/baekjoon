import sys

input = sys.stdin.readline

n = int(input())

S = set([])

for i in range(n):
    command = input().rstrip().split()

    if command[0] == "add":
        S.add(int(command[1]))
    elif command[0] == "remove":
        S.discard(int(command[1]))
    elif command[0] == "check":
        if int(command[1]) in S:
            print(1)
        else:
            print(0)
    elif command[0] == "toggle":
        if int(command[1]) in S:
            S.remove(int(command[1]))
        else:
            S.add(int(command[1]))

    elif command[0] == "all":
        S = set(range(1,21))
    elif command[0] == "empty":
        S = set([])
