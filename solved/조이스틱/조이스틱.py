name = input()

def cal(alphabet):
    num = ord(alphabet)
    if num-65 >= 13:
        return 91-num
    else:
        return num-65

def solution(name):

    names = [list(name), [list(name)[0]]+list(name)[1:][::-1]]
    answers = []
    for name in names:
        answer = 0
        i = 0
        while(True):

            if len(set(name)) == 1 and list(set(name))[0] == 'A':
                break

            if i >= 1:
                answer += 1
            
            answer += cal(name[i])
            name[i] = 'A'

            i+=1
        answers.append(answer)

    return min(answers)


print(solution(name))
