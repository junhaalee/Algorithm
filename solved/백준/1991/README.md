### 백준 - [1991](https://www.acmicpc.net/problem/1991)

### 풀이

*     A
*   /   \ 
*  B     C
* pre-order : A->B->C
* in-order : B->A->C
* post-order : B->C->A
* 재귀는 생각보다 단순하다

```Python

# 재귀 활용

# in-order
# B
if left.isalnum():
    path = inorder(left, path)
# A
path += node
# C
if right.isalnum():
    path = inorder(right, path)


# post-order
# B
if left.isalnum():
    path = inorder(left, path)
# C
if right.isalnum():
    path = inorder(right, path)
# A
path += node
```

