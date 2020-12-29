from collections import Counter

def solution(N, stages):

    stages.sort()
    result = dict(Counter(stages))

    prob = [[i+1,0] for i in range(N)]

    total = len(stages)
    for i in range(N):
        try:
            prob[i][1] = result[i+1]/total
            total -= result[i+1]
        except:
            pass

    temp = sorted(prob, key=(lambda x : x[1]), reverse=True)
    answer = []
    for t in temp:
        answer.append(t[0])

    return answer