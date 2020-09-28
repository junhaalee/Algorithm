def solution(n):

    answer = [1,2,3]

    for _ in range(n-3):
        del answer[0]
        answer.append(answer[-1]+answer[-2])

    return answer[-1]%1000000007