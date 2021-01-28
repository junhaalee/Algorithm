from collections import Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        task_dic = Counter(tasks)
        result = 0

        while True:
            sub = 0

            for t, _ in task_dic.most_common(n+1):
                sub += 1
                result += 1

                task_dic.subtract(t)
                task_dic += Counter()

            if not task_dic:
                break

            resut += n+1-sub

        return result
                
        

