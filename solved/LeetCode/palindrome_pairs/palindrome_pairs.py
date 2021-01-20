from collections import defaultdict
class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.word_id = -1
        self.palindrome_word_ids = list()

class Trie:
    def __init__(self):
        self.root = TrieNode()

    @staticmethod
    def is_palindrome(word):
        return word[::] == word[::-1]

    def insert(self, index, word):
        node = self.root
        for i, char in enumerate(reversed(word)):
            if self.is_palindrome(word[:len(word)-i]):
                node.palindrome_word_ids.append(index)
            node = node.children[char]
            # node.val = char
        node.word_id = index
    
    def search(self, index, word):
        result = list()
        node = self.root

        while word:
            # 3번
            if node.word_id >= 0:
                if self.is_palindrome(word):
                    result.append([index,node.word_id])
            if not word[0] in node.children:
                return result
            
            node = node.children[word[0]]
            word = word[1:]

        # 1번
        if node.word_id >= 0 and node.word_id != index:
            result.append([index, node.word_id])

        # 2번
        for palindrome_word_id in node.palindrome_word_ids:
            result.append([index,palindrome_word_id])
        
        return result

class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        trie = Trie()

        for i,word in enumerate(words):
            trie.insert(i,word)

        results = []

        for i, word in enumerate(words):
            results.extend(trie.search(i,word))
        
        return results
