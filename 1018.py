# m 가로 n 세로
h,w = map(int, input().split())

panel = []

for _ in range(h):
    panel.append(input())


def check(panel):

    case1 = 'WBWBWBWBBWBWBWBWWBWBWBWBBWBWBWBWWBWBWBWBBWBWBWBWWBWBWBWBBWBWBWBW'
    case2 = 'BWBWBWBWWBWBWBWBBWBWBWBWWBWBWBWBBWBWBWBWWBWBWBWBBWBWBWBWWBWBWBWB'

    count = 0

    if temp[0] == 'W':
        for i in range(len(case1)): 
            if case1[i] != temp[i] : count += 1
    else:
        for i in range(len(case2)): 
            if case2[i] != temp[i] : count += 1
    
    if count > 32 :
        return 64 - count
    else:
        return count

ans = []

for k in range(w-8+1):
    for j in range(h-8+1):
        temp = ''
        for i in range(8):
            temp += panel[i+j][k:k+8]
        ans.append(check(temp))

print(min(ans))