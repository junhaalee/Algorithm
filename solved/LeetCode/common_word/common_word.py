paragraph = "a, a, a, a, b,b,b,c, c"
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."

banned = ['hit']


import re
from collections import Counter

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        
        #banned에 포함되는 단어는 애초에 저장부터 안함
        words = [word for word in re.sub('[^\w]',' ',paragraph).lower().split()
                    if word not in banned]
        
        #most_common
        cnt = Counter(words)

        return cnt.most_common(1)[0][0]
        
