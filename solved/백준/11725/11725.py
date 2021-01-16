import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

n = int(input())
tree = [[] for _ in range(n+1)]

for _ in range(n-1):
    a,b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

parent = [0]*(n+1)
parent[1] = 1

def dfs(node,tree,parent):

    for child in tree[node]:
        if not parent[child]:
            parent[child] = node
            dfs(child,tree,parent)

dfs(1,tree,parent)

for i in range(2,n+1):
    print(parent[i])