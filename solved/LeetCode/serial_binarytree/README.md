### LeetCode - [Serialize and Deserialize Binary Tree](https://leetcode.com/problems/serialize-and-deserialize-binary-tree/)

### 풀이

* serialize(직렬화) - Tree(논리적 구조)를 배열(물리적 구조)로 변환
* deserialize(역직렬화) - 직렬화의 반대

```Python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        queue = deque([root])
        result = ['#']

        while queue:

            node = queue.popleft()

            if node:
                queue.append(node.left)
                queue.append(node.right)

                result.append(str(node.val))
            else:
                result.append('#')
            
        return result


    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        # 루트가 #이라면 return None
        if data[1] == '#':
            return None

        nodes = list(data)
        root = TreeNode(int(nodes[1]))
        queue = deque([root])
        # 루트의 자식 노드부터 시작
        index = 2

        while queue:

            node = queue.popleft()

            if nodes[index] is not '#':
                node.left = TreeNode(int(nodes[index]))
                queue.append(node.left)
            index += 1

            if nodes[index] is not '#':
                node.right = TreeNode(int(nodes[index]))
                queue.append(node.right)
            index += 1

        return root
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))

```

