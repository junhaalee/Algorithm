def solution(msg):
    
    answer = []
    dictionary = [chr(x) for x in range(65,91)]
    
    start = 0
    finish = 1
    while(True):            

        word = msg[start:finish]

        if finish == len(msg)+1:
            answer.append(dictionary.index(word)+1)
            break

        if word in dictionary:
            finish += 1
        else:
            dictionary.append(word)
            answer.append(dictionary.index(msg[start:finish-1])+1)
            start = finish-1

    return answer