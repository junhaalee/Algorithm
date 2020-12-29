def solution(people, limit):
    answer = len(people)
    people.sort()

    ind = 0
    while(True):
        
        if ind == len(people):
            break

        if people[ind] != 0:
            k = 1
            while(True):
                if ind+k == len(people):
                    break
                if people[-k] != 0  and people[ind]+people[-k] <= limit:
                    people[-k] = 0
                    answer -= 1
                    break
                else:
                    k += 1

        ind += 1

    return answer
