def solution(dartResult):
    dartResult = dartResult.replace('10','k')
    dart = ['10' if i == 'k' else i for i in dartResult]

    sdt = ['S','D','T']
    answer = []

    for d in dart:
        if d in sdt:
            answer[-1] = answer[-1]**(sdt.index(d)+1)
        elif d == '#':
            answer[-1] *= -1
        elif d == '*':
            answer[-1] *= 2
            try:
                answer[-2] *= 2
            except:
                pass
        else:
            answer.append(int(d))

    return sum(answer)