### 백준 - [1613](https://www.acmicpc.net/problem/1613)

### 풀이

* 그래프에서 정점끼리의 최단 경로를 구하는 문제
* -하나의 정점에서 다른 하나의 최단 경로를 구하는 문제
* -하나의 정점에서 다른 모든 정점까지의 최단 경로를 구하는 문제 -> 다익스트라 알고리즘
* -하나의 목적지로 가는 모든 최단 경로를 구하는 문제
* -모든 최단 경로를 구하는 문제 -> 플로이드-와샬 알고리즘


* 플로이드-와샬 알고리즘
* 모든 경로에 대한 비용을 저장하는 테이블, 각 정점까지 가기 직전의 정점을 저장한 테이블을 이용하여 이차원 배열 구성

```Python
# 그래프 구성
for _ in range(k):
    a,b = map(int, input().split())
    graph[a-1][b-1] = 1

# 모든 정점 k에 대해서 
# k를 거쳐가는 경로 이어주기
# i->k / k->j 일 때, i->j
for k in range(n):
    for i in range(n):
        for j in range(n):
            if graph[i][k] and graph[k][j]:
                graph[i][j] = 1
```

