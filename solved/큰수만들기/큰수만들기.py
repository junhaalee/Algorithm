def solution(number, k):
    answer = ''
    n,k = len(number)-k,len(number)-k

    while(True):
        if len(answer) == n:
            break
        if len(number) > k:
            if k == 1:
                answer += max(number[:])
            else:
                answer += max(number[:-k+1])
                ind = number.index(max(number[:-k+1]))
            number = number[ind+1:]
            k -= 1
        else:
            answer += number

    return answer