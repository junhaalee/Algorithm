### 백준 - [11725](https://www.acmicpc.net/problem/11725)

### 풀이

* 먼저 양뱡향 그래프로 tree를 구성하고 그래프를 순회하면서 parent 체크를 안한 노드에 parent를 할당

* 첫 풀이가 왜 틀렸는지 모르겠다

```Python
# 첫 풀이
tree = {1:None}

for _ in range(n-1):
    a,b = map(int,input().split())
    if a not in tree:
        tree[a] = b
    else:
        tree[b] = a

for i in range(2,n+1):
    print(tree[i])


# DFS
parent = [0]*(n+1)
parent[1] = 1

def dfs(node,tree,parent):

    for child in tree[node]:
        # 아직 parent가 정해지지 않았다면 parent 정해주기
        # 이미 parent가 정해져있다면 Pass
        if not parent[child]:
            parent[child] = node
            dfs(child,tree,parent)

```