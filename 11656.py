string = input().rstrip()

answer = [string[i:] for i in range(len(string))]

print("\n".join(sorted(answer)))