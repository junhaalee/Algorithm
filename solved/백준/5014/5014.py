import sys 
from collections import deque
f, s, g, u, d = map(int, sys.stdin.readline().split()) 

def bfs(): 
    queue = deque([(s, 0)]) 
    visit = [0] * (f+1) 
    visit[s] = 1
    while queue: 
        q, c = queue.popleft() 
        if q == g: 
            return c 
        c += 1 
        if q-d >= 1 and not visit[q-d]: 
            visit[q-d] = 1 
            queue.append((q-d, c)) 
        if q+u <= f and not visit[q+u]: 
            visit[q+u] = 1 
            queue.append((q+u, c)) 
    return -1

ans = bfs() 
if ans >= 0: 
    print(ans) 
else: 
    print("use the stairs")