### LeetCode - [Task Scheduler](https://leetcode.com/problems/task-scheduler/)

### 풀이

* counter를 활용한 우선순위 큐
* 꿀팁 : 빈 Counter()를 더할 경우, 0 이하인 아이템을 목록에서 제거 

```Python

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
                # 0 이하인 아이템을 목록에서 제거
                task_dic += Counter()

            if not task_dic:
                break

            # idle 개수 추가
            resut += n+1-sub

        return result

```

