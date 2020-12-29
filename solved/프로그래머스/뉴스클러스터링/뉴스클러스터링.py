
def word(s):
    
    result = []
    ind = 0
    while(ind < len(s)-1):

        if (64 < ord(s[ind].upper()) < 91) and (64 < ord(s[ind+1].upper()) < 91):
            temp = s[ind].upper()+s[ind+1].upper()
            result.append(temp)

        ind += 1
    
    return result



def solution(str1, str2):

    str_1 = word(str1)
    str_2 = word(str2)
    
    inter, uni = 0,0

    intersection = list(set(str_1)&set(str_2))
    union = list(set(str_1+str_2))
    
    for i in intersection:
        inter += min([str_1.count(i),str_2.count(i)])
    
    for u in union:
        uni += max([str_1.count(u),str_2.count(u)])

    if len(union) == len(intersection) == 0:
        answer = 65536
    else:
        answer = int(65536*inter/uni)
    
    return answer
