import sys
input = sys.stdin.readline

ans,count = 0,1
while(count<=8):

    temp = list(input().strip())

    if count%2:
        ans += temp[::2].count('F')

    else:
        ans += temp[1::2].count('F')

    count += 1
    
print(ans)
