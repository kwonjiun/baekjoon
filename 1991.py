import sys

input = sys.stdin.readline

n = int(input())

tree = {}

for i in range(n):
    node, left, right = input().rstrip().split()
    tree[node] = [left, right]

def pre(node: str):
    if node != '.':
        print(node, end= '')
        pre(tree[node][0])
        pre(tree[node][1])

def ino(node : str):
    if node != '.':
        ino(tree[node][0])
        print(node, end= '')
        ino(tree[node][1])

def post(node : str):
    if node != '.':
        post(tree[node][0])
        post(tree[node][1])
        print(node, end= '')

pre('A')
print()
ino('A')
print()
post('A')