from collections import deque
import sys
input = sys.stdin.readline

def bfs(x,y):
    que, current = deque(),[]
    que.append([x,y,20])
    current.append([x,y,20])

    while que:
        x,y,b = que.popleft()
        if x == tx and y == tx:
            print('happy')
            return
        for nx, ny in D:
            if [nx, ny, 20] not in current:
                l = abs(ny-y) + abs(nx-x)
                if b*50 >= l:
                    que.append([nx,ny,20])
                    current.append([nx,ny,20])
    print('sad')
    return

for _ in range(int(input())):
    n = int(input())
    dx,dy = map(int, input().split())
    D = []
    for _ in range(n):
        D.append(list(map(int, input().split())))

    tx,ty = map(int, input().split())
    D.append([tx,ty])
    bfs(dx,dy)