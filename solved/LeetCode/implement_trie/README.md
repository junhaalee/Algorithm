### LeetCode - [Implement Trie (Prefix Tree)](https://leetcode.com/problems/implement-trie-prefix-tree/)

### 풀이

* 트라이(Trie) : 문자열 탐색을 위한 자료구조 - 다진 트리의 형태

```Python
class TrieNode:
    def __init__(self):
        self.word = False
        self.children = collections.defaultdict(TrieNode)

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self,word):
        node = self.root
        # 단어의 한 글자씩 깊이 탐색
        for char in word:
            node = node.children[char]
        # 마지막 글자에 대해서만 True
        node.word = True
    
    def search(self, word):
        node = self.root
        for char in word:
            # children 중에 다음 글자가 없으면 return False
            if char not in node.children:
                return False
            node = node.children[char]
        # 끝까지 도달했으면 node.word를 return
        return node.word
    
    def startsWith(self, pre):
        node = self.root
        for char in pre:
            if char not in node.children:
                return False
            node = node.children[char]
        
        # search랑은 다르게 주어진 pre에 대해서 탐색할 수 있을 때까지 탐색하고
        # 결과 return
        return True

```

