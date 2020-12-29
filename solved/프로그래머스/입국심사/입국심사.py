def solution(n, times):
    
    left = 0
    right = n*max(times)

    while left<=right:
        
        mid = (left+right)//2

        temp = [mid//t for t in times]

        if sum(temp) >= n:
            answer = mid 
            right = mid-1
        else:
            left = mid+1
    
    return answer