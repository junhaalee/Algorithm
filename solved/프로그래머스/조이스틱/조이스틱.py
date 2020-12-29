def cal(alphabet):
    num = ord(alphabet)
    if num-65 >= 13:
        return 91-num
    else:
        return num-65

def solution(name):
    
    name = list(name)
    answer = 0
    ind = 0

    while(True):
        
        answer += cal(name[ind])
        name[ind] = 'A'
        
        if len(set(name)) == 1 and list(set(name))[0] == 'A':
            break

        left,right,indL,indR = 1,1,ind-1,ind+1

        while(True):
            if name[indL] != 'A':
                break
            indL -= 1
            left += 1
        while(True):
            if name[indR] != 'A':
                break            
            indR += 1
            right += 1            
            
        if left < right:
            answer += left
            ind = indL
        else:
            answer += right
            ind = indR

    return answer