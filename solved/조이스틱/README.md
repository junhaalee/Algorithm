### 프로그래머스  - [조이스틱](https://programmers.co.kr/learn/courses/30/lessons/42860)

### 풀이

* 한쪽 방향으로 계속 직진하는 것이 아니라, 방향을 바꿔야 하는 경우가 있음.

```Python
        left,right,indL,indR = 1,1,ind-1,ind+1

        while(True):
            if name[indL] != 'A':
                break
            indL -= 1
            left += 1
        while(True):
            if name[indR] != 'A':
                break            
            indR += 1
            right += 1       
```

