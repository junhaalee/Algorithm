import sys
input = sys.stdin.readline

n,m,t = map(int, input().split())
graph = []

for _ in range(n):
    graph.append(list(map(int, input().split())))

dx = [1,0,-1,0]
dy = [0,1,0,-1]

count = 0
visit = [[0,0]]
check = False
check_count = 10000
while(True):

    if [n-1,m-1] in visit or count > t:
        break

    temp = []

    for v in visit:
        x,y = v[0],v[1]
        for i in range(4):
            tx,ty = x+dx[i], y+dy[i]
            if (0<=tx<n) and (0<=ty<m):
                if graph[tx][ty] == 0:
                    graph[tx][ty] = 1
                    temp.append([tx,ty])
                elif graph[tx][ty] == 2:
                    sw = [tx,ty]
                    graph[tx][ty] = 1
                    check_count = count+1
                    check = True

    visit = temp
    count += 1

count = min(count, check_count+(n+m-2)-sw[0]-sw[1]) if check else count

if count > t:
    print('Fail')
else:
    print(count)