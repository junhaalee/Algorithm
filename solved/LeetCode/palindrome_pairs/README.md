### LeetCode - [Palindrome Pairs](https://leetcode.com/problems/palindrome-pairs/)

### 풀이

* 굉장히 어려움
* 1번 : 끝까지 탐색했을 때, word_id가 있는 경우
* 2번 : 끝까지 탐색했을 때, palindrom_word_ids가 있는 경우
* 3번 : 탐색 중간에 word_id가 있고 나머지 문자가 팰린드롬인 경우

```Python
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

```

