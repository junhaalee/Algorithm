def solution(numbers, target):

    ans = [0]

    for num in numbers:
        temp = []
        for a in ans:
            temp.append(a+num)
            temp.append(a-num)
        ans = temp

    answer = temp.count(target)

    return answer
