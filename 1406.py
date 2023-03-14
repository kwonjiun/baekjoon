import sys

string1 = list(sys.stdin.readline().rstrip())

string2 = []

n = int(sys.stdin.readline())

for i in range(n):
    command = sys.stdin.readline().split()
    if command[0] == "L" and len(string1) != 0:
            string2.append(string1.pop())
    elif command[0] == "D" and len(string2) != 0:
        string1.append(string2.pop())
    elif command[0] == "B" and len(string1) != 0:
        string1.pop()
    elif command[0] == "P":
        string1.append(command[1])

print(''.join(string1 + list(reversed(string2))))