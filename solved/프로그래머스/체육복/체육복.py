def solution(n, lost, reserve):

    answer = n-len(lost)

    for k in range(len(lost)):
        for i in range(len(reserve)):
            if lost[k] == reserve[i]:
                lost[k],reserve[i] = 45,35
                answer += 1

    for k in range(len(reserve)):
        ind = 0
        while(True):
            if ind == len(lost):
                break
            if reserve[k]-1 == lost[ind]:
                answer += 1
                lost[ind],reserve[k] = 45,35
                break
            else:
                ind += 1
    
    for k in range(len(reserve)):
        ind = 0
        while(True):
            if ind == len(lost):
                break
            if reserve[k]+1 == lost[ind]:
                answer += 1
                lost[ind],reserve[k] = 45,35
                break
            else:
                ind += 1     
                        
    return answer


print(solution(n,lost,reserve))