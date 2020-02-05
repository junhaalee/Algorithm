test = int(input())

for i in range(test):
    info = list(map(int, input().split()))
    students = info[0]
    score = info[1:]
    avg = sum(score)/students
    count = 0
    for j in range(students):
        if score[j]>avg:
            count+=1
    print(str('%.3f' % round(count / info[0] * 100, 3)) + '%')    