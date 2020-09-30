def solution(land):
    
    for ind in range(1, len(land)):
        
        temp = land[ind-1]
        
        for i in range(4):
            land[ind][i] += max(temp[:i]+temp[i+1:])

    return max(land[-1])