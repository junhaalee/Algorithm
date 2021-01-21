### LeetCode - [Largest Number](https://leetcode.com/problems/largest-number/)

### 풀이

* Insertion Sort 활용
* 프로그래머스
* https://programmers.co.kr/learn/courses/30/lessons/42746 와 똑같은 문제

```Python

# 1. 프로그래머스 풀이 - 32ms
def solution(numbers):
    numbers = sorted(list(map(str,numbers)), key = lambda x : x*3, reverse = True)
    return str(int(''.join(numbers)))


# 2. 삽입 정렬 활용 - 64ms
class Solution:
    def swap(self, n1, n2):
        return str(n1)+str(n2) < str(n2)+str(n1)

    def largestNumber(self, nums: List[int]) -> str:
        i = 1
        while i < len(nums):
            j = i
            while j > 0 and self.swap(nums[j-1],nums[j]):
                nums[j-1], nums[j] = nums[j], nums[j-1]
                j -= 1
            i += 1
        
        return str(int(''.join(map(str,nums))))

```

