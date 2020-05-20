### 백준  - [1094](https://www.acmicpc.net/problem/1094)

### 풀이

* 가격이 주어졌을 때, 동전의 개수를 최소로하는 방법을 구하는 문제랑 같은 방식으로 풀었다.
* 64가 아니라면, nums라는 배열을 2로 나눠주면 만들어주고 풀면 될 것 같다.

```Python
n, count = int(input()), 0
nums = [64,32,16,8,4,2,1]
ind = 0
while(n):

    if nums[ind] <= n:
        count += n//nums[ind]
        n %= nums[ind]
    ind += 1

print(count)
```

