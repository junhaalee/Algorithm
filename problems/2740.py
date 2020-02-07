fn, fm = map(int, input().split())
fir = [list(map(int, input().split())) for _ in range(fn)]

sn, sm = map(int, input().split())
sec = [list(map(int, input().split())) for _ in range(sn)]
ans = []

for i in range(fn):

    re = []

    for j in range(sm):

        temp = []
        
        for k in range(sn):
            temp.append(sec[k][j])

        sol = []

        for f,s in zip(fir[i],temp):
            sol.append(f*s)

        re.append(sum(sol))

    ans.append(re)

for a in ans:
    result = ''
    for i in range(len(a)):
        result += str(a[i])+' '
    print(result[:-1])