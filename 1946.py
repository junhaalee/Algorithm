T = int(input())

for _ in range(T):

    n = int(input())

    case = []

    for i in range(n):
        case.append(list(map(int, input().split())))

    case = sorted(case, key = lambda x : -x[0])

    sec = []

    for i in range(n):
        sec.append(case[i][1])

    count = 1

    for i in range(n-1):
        for j in range(i, n):
            if sec[i] > sec[j]:
                break
            if sec[i] < sec[j] and j == n-1:
                count += 1
            
    print(count)