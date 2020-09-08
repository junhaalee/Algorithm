### 프로그래머스 - [캐시](https://programmers.co.kr/learn/courses/30/lessons/17680)

### 풀이

* LRU(Leaset Recently Used) - 캐시 교체 알고리즘
* 자세한 설명 - https://jins-dev.tistory.com/entry/LRU-Cache-Algorithm-%EC%A0%95%EB%A6%AC
* list에서 특정 원소를 제거하고자 할 때, remove를 사용하자...

```Python
temp = [1,2,3,4]

temp.remove(2)

temp = [1,3,4]
```

