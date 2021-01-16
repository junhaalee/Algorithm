import sys
input = sys.stdin.readline

n = int(input())

tree = dict()

for _ in range(n):
    node, left, right = map(str,input().split())
    tree[node] = [left, right]

def preorder(node, path):

    path += node

    left = tree[node][0]
    right = tree[node][1]

    if left.isalnum():
        path = preorder(left, path)
    if right.isalnum():
        path = preorder(right, path)

    return path

def inorder(node, path):

    left = tree[node][0]
    right = tree[node][1]

    if left.isalnum():
        path = inorder(left, path)
    
    path += node

    if right.isalnum():
        path = inorder(right, path)

    return path

def postorder(node, path):

    left = tree[node][0]
    right = tree[node][1]

    if left.isalnum():
        path = postorder(left, path)
    
    if right.isalnum():
        path = postorder(right, path)

    path += node

    return path

print(preorder('A',''))
print(inorder('A',''))
print(postorder('A',''))