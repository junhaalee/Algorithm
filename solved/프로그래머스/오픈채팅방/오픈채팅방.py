import re
p = re.compile('[a-zA-Z0-9]+')

def solution(record):
    
    enter = '님이 들어왔습니다.'
    leave = '님이 나갔습니다.'

    answer = []

    dic = dict()

    for rec in record:

        if len(rec.split()) == 3:

            com, uid, name = rec.split()

            if com == 'Enter':
                dic[uid] = name
                answer.append(str(uid)+enter)
            else:
                dic[uid] = name

        else:
            com, uid = rec.split()
            answer.append(str(uid)+leave)
        
    for i in range(len(answer)):
        uid = p.findall(answer[i])[0]
        answer[i] = answer[i].replace(uid,dic[uid])

    return answer