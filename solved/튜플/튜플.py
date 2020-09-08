def solution(s):

    answer = []

    temp = sorted([x for x in s[2:-2].replace('},{',' ').split()], key = (lambda x : len(x)))

    for i in range(len(temp)):
        numbers = list(map(int, temp[i].split(',')))
        for number in numbers:
            if number not in answer:
                answer.append(number)

    return answer