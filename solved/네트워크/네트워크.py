def dfs(current, visit, graph):

    visit.append(current)

    for next in range(len(graph[current])):
        if graph[current][next] and next not in visit:
            visit = dfs(next,visit,graph)
    
    return visit

def solution(n, computers):
    answer = []

    for i in range(n):
        ans = dfs(i,[],computers)
        ans.sort()
        if ans not in answer:
            answer.append(ans)

    return len(answer)
