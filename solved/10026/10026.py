import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

n = int(input())
graph = []
p_graph = []
for _ in range(n):
    graph.append(list(input()))

for i in range(len(graph)):
    temp = []
    for k in range(len(graph[i])):
        temp.append('R') if graph[i][k] == 'G' else temp.append(graph[i][k])
    p_graph.append(temp)

dx = [0,1,0,-1]
dy = [1,0,-1,0]

c_graph = [[1]*n for _ in range(n)]
c_p_graph = [[1]*n for _ in range(n)]

def dfs(graph,visit,current,check_graph):
    
    x,y = current[0],current[1]
    visit.append(current)
    
    if check_graph[x][y]:
        check_graph[x][y] = 0
        for i in range(4):
            tx = x+dx[i]
            ty = y+dy[i]

            if tx >= 0 and ty >= 0 and tx < n and ty < n and graph[tx][ty] != 0 and graph[x][y] == graph[tx][ty] and check_graph[tx][ty]:
                next = [tx,ty]
                dfs(graph,visit,next,check_graph)
        
        return visit
    else:
        return 0

ans1 = []
ans2 = []
for i in range(n):
    for k in range(n):
        temp1 = dfs(graph,[],[i,k],c_graph)
        temp2 = dfs(p_graph,[],[i,k],c_p_graph)
        if temp1:
            ans1.append(temp1)
        if temp2:
            ans2.append(temp2)

print(len(ans1),len(ans2))