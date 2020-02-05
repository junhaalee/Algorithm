n = int(input())

def cal(n):
    temp = 0
    for i in range(n+1):
        temp+=i
    return temp

for i in range(n):
    score = input().split('X')
    val = 0
    for j in range(len(score)):
        val += cal(len(score[j]))
    print(val)
    